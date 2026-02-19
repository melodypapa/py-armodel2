"""PerInstanceMemory AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 597)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PerInstanceMemory.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    String,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class PerInstanceMemory(Identifiable):
    """AUTOSAR PerInstanceMemory."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    init_value: Optional[String]
    sw_data_def: Optional[SwDataDefProps]
    type: Optional[CIdentifier]
    type_definition: Optional[String]
    def __init__(self) -> None:
        """Initialize PerInstanceMemory."""
        super().__init__()
        self.init_value: Optional[String] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.type: Optional[CIdentifier] = None
        self.type_definition: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PerInstanceMemory":
        """Deserialize XML element to PerInstanceMemory object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PerInstanceMemory object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse init_value
        child = ARObject._find_child_element(element, "INIT-VALUE")
        if child is not None:
            init_value_value = child.text
            obj.init_value = init_value_value

        # Parse sw_data_def
        child = ARObject._find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        # Parse type
        child = ARObject._find_child_element(element, "TYPE")
        if child is not None:
            type_value = child.text
            obj.type = type_value

        # Parse type_definition
        child = ARObject._find_child_element(element, "TYPE-DEFINITION")
        if child is not None:
            type_definition_value = child.text
            obj.type_definition = type_definition_value

        return obj



class PerInstanceMemoryBuilder:
    """Builder for PerInstanceMemory."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PerInstanceMemory = PerInstanceMemory()

    def build(self) -> PerInstanceMemory:
        """Build and return PerInstanceMemory object.

        Returns:
            PerInstanceMemory instance
        """
        # TODO: Add validation
        return self._obj
