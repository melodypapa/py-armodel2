"""McDataAccessDetails AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
        RTEEvent,
    )



class McDataAccessDetails(ARObject):
    """AUTOSAR McDataAccessDetails."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rte_event_refs: list[RTEEvent]
    variable_accesses: list[VariableAccess]
    def __init__(self) -> None:
        """Initialize McDataAccessDetails."""
        super().__init__()
        self.rte_event_refs: list[RTEEvent] = []
        self.variable_accesses: list[VariableAccess] = []

    def serialize(self) -> ET.Element:
        """Serialize McDataAccessDetails to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize rte_event_refs (list to container "RTE-EVENT-REFS")
        if self.rte_event_refs:
            wrapper = ET.Element("RTE-EVENT-REFS")
            for item in self.rte_event_refs:
                serialized = SerializationHelper.serialize_item(item, "RTEEvent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize variable_accesses (list to container "VARIABLE-ACCESSES")
        if self.variable_accesses:
            wrapper = ET.Element("VARIABLE-ACCESSES")
            for item in self.variable_accesses:
                serialized = SerializationHelper.serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McDataAccessDetails":
        """Deserialize XML element to McDataAccessDetails object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McDataAccessDetails object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse rte_event_refs (list from container "RTE-EVENT-REFS")
        obj.rte_event_refs = []
        container = SerializationHelper.find_child_element(element, "RTE-EVENT-REFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rte_event_refs.append(child_value)

        # Parse variable_accesses (list from container "VARIABLE-ACCESSES")
        obj.variable_accesses = []
        container = SerializationHelper.find_child_element(element, "VARIABLE-ACCESSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.variable_accesses.append(child_value)

        return obj



class McDataAccessDetailsBuilder:
    """Builder for McDataAccessDetails."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McDataAccessDetails = McDataAccessDetails()

    def build(self) -> McDataAccessDetails:
        """Build and return McDataAccessDetails object.

        Returns:
            McDataAccessDetails instance
        """
        # TODO: Add validation
        return self._obj
