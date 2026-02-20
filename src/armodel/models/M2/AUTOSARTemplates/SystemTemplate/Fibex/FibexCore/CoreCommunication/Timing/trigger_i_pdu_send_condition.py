"""TriggerIPduSendCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 399)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class TriggerIPduSendCondition(ARObject):
    """AUTOSAR TriggerIPduSendCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize TriggerIPduSendCondition."""
        super().__init__()
        self.mode_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize TriggerIPduSendCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize mode_refs (list to container "MODE-REFS")
        if self.mode_refs:
            wrapper = ET.Element("MODE-REFS")
            for item in self.mode_refs:
                serialized = ARObject._serialize_item(item, "ModeDeclaration")
                if serialized is not None:
                    child_elem = ET.Element("MODE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TriggerIPduSendCondition":
        """Deserialize XML element to TriggerIPduSendCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TriggerIPduSendCondition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse mode_refs (list from container "MODE-REFS")
        obj.mode_refs = []
        container = ARObject._find_child_element(element, "MODE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_refs.append(child_value)

        return obj



class TriggerIPduSendConditionBuilder:
    """Builder for TriggerIPduSendCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerIPduSendCondition = TriggerIPduSendCondition()

    def build(self) -> TriggerIPduSendCondition:
        """Build and return TriggerIPduSendCondition object.

        Returns:
            TriggerIPduSendCondition instance
        """
        # TODO: Add validation
        return self._obj
