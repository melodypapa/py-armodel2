"""ModeRequestTypeMap AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 44)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 115)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )



class ModeRequestTypeMap(ARObject):
    """AUTOSAR ModeRequestTypeMap."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    implementation: Optional[AbstractImplementationDataType]
    mode_group_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeRequestTypeMap."""
        super().__init__()
        self.implementation: Optional[AbstractImplementationDataType] = None
        self.mode_group_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeRequestTypeMap":
        """Deserialize XML element to ModeRequestTypeMap object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeRequestTypeMap object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse implementation
        child = ARObject._find_child_element(element, "IMPLEMENTATION")
        if child is not None:
            implementation_value = ARObject._deserialize_by_tag(child, "AbstractImplementationDataType")
            obj.implementation = implementation_value

        # Parse mode_group_ref
        child = ARObject._find_child_element(element, "MODE-GROUP")
        if child is not None:
            mode_group_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.mode_group_ref = mode_group_ref_value

        return obj



class ModeRequestTypeMapBuilder:
    """Builder for ModeRequestTypeMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeRequestTypeMap = ModeRequestTypeMap()

    def build(self) -> ModeRequestTypeMap:
        """Build and return ModeRequestTypeMap object.

        Returns:
            ModeRequestTypeMap instance
        """
        # TODO: Add validation
        return self._obj
