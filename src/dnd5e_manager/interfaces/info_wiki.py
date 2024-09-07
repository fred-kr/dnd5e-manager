from dnd5e_srd_api.api_interface import (
    APIReference,
    EquipmentCategoriesIndex,
    get,
    get_item_from_reference,
    get_items_in_category,
)
from PySide6 import QtCore, QtWidgets

from ...ui.ui_wiki_interface import Ui_WikiInterface
from ..models.resource_index_model import ResourceIndexModel


class InfoWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("info_widget")

        self.ui = Ui_WikiInterface()
        self.ui.setupUi(self)

        self._setup_pivot()
        self._setup_search()
        self._setup_list_view()
        self._connect_qsignals()

    def _connect_qsignals(self) -> None:
        self.ui.line_edit_filter.textEdited.connect(self.search_equipment)

    def _setup_pivot(self) -> None:
        self.ui.pivot_nav_bar.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        for page in [self.ui.page_database_search, self.ui.page_app_info]:
            obj_name = page.objectName()
            label_txt = obj_name.removeprefix("page_").replace("_", " ").title()

            self.ui.pivot_nav_bar.addItem(
                routeKey=obj_name,
                text=label_txt,
                onClick=lambda _, page=page: self.ui.stacked_info_page.setCurrentWidget(page),
            )

        self.ui.stacked_info_page.currentChanged.connect(self._on_page_changed)
        self.ui.stacked_info_page.setCurrentWidget(self.ui.page_database_search)
        self.ui.pivot_nav_bar.setCurrentItem(self.ui.page_database_search.objectName())

    @QtCore.Slot(int)
    def _on_page_changed(self, index: int) -> None:
        widget = self.ui.stacked_info_page.widget(index)
        self.ui.pivot_nav_bar.setCurrentItem(widget.objectName())

    def _setup_search(self) -> None:
        api_data = get("/api/equipment-categories").json()["results"]
        ref_list: list[APIReference[EquipmentCategoriesIndex]] = []
        for api_ref_dict in api_data:
            idx = EquipmentCategoriesIndex(api_ref_dict["index"])
            ref_list.append(
                APIReference(
                    index=idx,
                    name=api_ref_dict["name"],
                    url=api_ref_dict["url"],
                )
            )

        self.equipment_list = ResourceIndexModel(ref_list)
        completer = QtWidgets.QCompleter()
        completer.setCompletionRole(QtCore.Qt.ItemDataRole.DisplayRole)
        completer.setModelSorting(QtWidgets.QCompleter.ModelSorting.CaseInsensitivelySortedModel)
        completer.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        completer.setModel(self.equipment_list)
        self.ui.line_edit_filter.setCompleter(completer)

    def _setup_list_view(self) -> None:
        self.ui.list_view_api.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.list_view_api.doubleClicked.connect(self.search_for_reference)
        self.ui.bc_bar_item_list.currentItemChanged.connect(print)

    @QtCore.Slot(str)
    def search_equipment(self, text: str) -> None:
        api_ref = self.equipment_list.item_from_name(text)
        if not api_ref:
            self.ui.list_view_api.setModel(None)
            self._category_data = None
            return

        category_index = EquipmentCategoriesIndex(api_ref.index)

        category_data = get_items_in_category(category_index)
        if not category_data:
            self.ui.list_view_api.setModel(None)
            self._category_data = None
            return
        self._category_data = category_data

        self.ui.list_view_api.setModel(ResourceIndexModel(category_data))

    @QtCore.Slot(QtCore.QModelIndex)
    def search_for_reference(self, index: QtCore.QModelIndex) -> None:
        if api_ref := self.ui.list_view_api.model().data(index, role=QtCore.Qt.ItemDataRole.UserRole):
            item_data = get_item_from_reference(api_ref)

            # Markdown description
            desc_str = "\n\n".join(desc) if (desc := item_data.desc) else "No description available."
            self.ui.text_browser_search_result.setMarkdown(f"# {item_data.name}\n\n{desc_str}")

            # Breadcrumbs
            url = item_data.url
            parts = url.removeprefix("/").split("/")
            self.ui.bc_bar_item_list.clear()
            for part in parts:
                self.ui.bc_bar_item_list.addItem(routeKey=part, text=part.title())
