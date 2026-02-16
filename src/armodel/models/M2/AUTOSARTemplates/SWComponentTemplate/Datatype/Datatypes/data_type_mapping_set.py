"""DataTypeMappingSet AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_map import (
    DataTypeMap,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_request_type_map import (
    ModeRequestTypeMap,
)


class DataTypeMappingSet(ARElement):
    """AUTOSAR DataTypeMappingSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_type_maps": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DataTypeMap,
        ),  # dataTypeMaps
        "mode_request_type_maps": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ModeRequestTypeMap,
        ),  # modeRequestTypeMaps
    }

    def __init__(self) -> None:
        """Initialize DataTypeMappingSet."""
        super().__init__()
        self.data_type_maps: list[DataTypeMap] = []
        self.mode_request_type_maps: list[ModeRequestTypeMap] = []


class DataTypeMappingSetBuilder:
    """Builder for DataTypeMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataTypeMappingSet = DataTypeMappingSet()

    def build(self) -> DataTypeMappingSet:
        """Build and return DataTypeMappingSet object.

        Returns:
            DataTypeMappingSet instance
        """
        # TODO: Add validation
        return self._obj
