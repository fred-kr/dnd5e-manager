from dnd5e_srd_api.api_interface import API
from PySide6 import QtCore, QtWidgets

from ...ui.ui_wiki_interface import Ui_WikiInterface
from ..models.resource_index_model import APIReferenceListModel


class InfoWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("info_widget")

        self.setStyleSheet(
            "QComboBox { min-width: 150px; min-height: 31px; padding-left: 10px; }"
            "QComboBox QAbstractItemView::item { min-height: 31px; }"
        )
        self.ui = Ui_WikiInterface()
        self.ui.setupUi(self)

        self.api = API()
        self.root_endpoints_model = QtCore.QStringListModel(["Character Data", "Equipment", "Spells"])
        self.ui.combo_box_category.setModel(self.root_endpoints_model)

        self._setup_pivot()
        self._setup_list_view()
        self._connect_qsignals()

    def _connect_qsignals(self) -> None:
        # self.ui.line_edit_filter.textEdited.connect(self.search_resource)
        self.ui.combo_box_category.currentTextChanged.connect(self.show_endpoint_resources)

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

    def _setup_list_view(self) -> None:
        self.ui.list_view_api.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.list_view_api.doubleClicked.connect(self.get_resource_data)

    @QtCore.Slot(str)
    def show_endpoint_resources(self, text: str) -> None:
        if text == "Character Data":
            endpoint = self.api.character_data
        elif text == "Equipment":
            endpoint = self.api.equipment
        elif text == "Spells":
            endpoint = self.api.spells
        else:
            return
        # resource_index = endpoint.get_available_resources()
        self.resource_index_model = APIReferenceListModel(resource_index)
        self.ui.list_view_api.setModel(self.resource_index_model)

        completer = QtWidgets.QCompleter()
        completer.setCompletionRole(QtCore.Qt.ItemDataRole.DisplayRole)
        completer.setModelSorting(QtWidgets.QCompleter.ModelSorting.CaseInsensitivelySortedModel)
        completer.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        completer.setModel(self.resource_index_model)
        self.ui.line_edit_filter.setCompleter(completer)

    # @QtCore.Slot(str)
    # def search_resource(self, text: str) -> None:
    #     api_ref = self.
    #     if not api_ref:
    #         self.ui.list_view_api.setModel(None)
    #         self._category_data = None
    #         return

    #     category_index = EquipmentCategoriesIndex(api_ref.index)

    #     category_data = get_items_in_category(category_index)
    #     if not category_data:
    #         self.ui.list_view_api.setModel(None)
    #         self._category_data = None
    #         return
    #     self._category_data = category_data

    #     self.ui.list_view_api.setModel(ResourceIndexModel(category_data))

    @QtCore.Slot(QtCore.QModelIndex)
    def get_resource_data(self, index: QtCore.QModelIndex) -> None:
        cd = self.character_data
        resource_index = self.resource_index_model.data(index, role=QtCore.Qt.ItemDataRole.UserRole)
        if isinstance(resource_index, cd.AbilityScores):
            data = cd.get_ability_score(resource_index)
        elif isinstance(resource_index, cd.Alignments):
            data = cd.get_alignment(resource_index)
        elif isinstance(resource_index, cd.Backgrounds):
            data = cd.get_background(resource_index)
        elif isinstance(resource_index, cd.Languages):
            data = cd.get_language(resource_index)
        elif isinstance(resource_index, cd.Proficiencies):
            data = cd.get_proficiency(resource_index)
        elif isinstance(resource_index, cd.Skills):
            data = cd.get_skill(resource_index)
        else:
            return

        description = getattr(data, "desc", None)

        # Markdown description
        desc_str = "\n\n".join(description) if isinstance(description, list) else "No description available"
        self.ui.text_browser_search_result.setMarkdown(f"# {data.name}\n\n{desc_str}")
