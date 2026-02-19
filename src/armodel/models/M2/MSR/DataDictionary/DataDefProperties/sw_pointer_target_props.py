"""SwPointerTargetProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 39)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 286)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 471)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
        BswModuleEntry,
    )
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class SwPointerTargetProps(ARObject):
    """AUTOSAR SwPointerTargetProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    function_pointer: Optional[BswModuleEntry]
    sw_data_def: Optional[SwDataDefProps]
    target_category: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize SwPointerTargetProps."""
        super().__init__()
        self.function_pointer: Optional[BswModuleEntry] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.target_category: Optional[Identifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwPointerTargetProps":
        """Deserialize XML element to SwPointerTargetProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwPointerTargetProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse function_pointer
        child = ARObject._find_child_element(element, "FUNCTION-POINTER")
        if child is not None:
            function_pointer_value = ARObject._deserialize_by_tag(child, "BswModuleEntry")
            obj.function_pointer = function_pointer_value

        # Parse sw_data_def
        child = ARObject._find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        # Parse target_category
        child = ARObject._find_child_element(element, "TARGET-CATEGORY")
        if child is not None:
            target_category_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.target_category = target_category_value

        return obj



class SwPointerTargetPropsBuilder:
    """Builder for SwPointerTargetProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwPointerTargetProps = SwPointerTargetProps()

    def build(self) -> SwPointerTargetProps:
        """Build and return SwPointerTargetProps object.

        Returns:
            SwPointerTargetProps instance
        """
        # TODO: Add validation
        return self._obj
