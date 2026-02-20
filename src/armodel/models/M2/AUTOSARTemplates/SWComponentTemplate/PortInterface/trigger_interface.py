"""TriggerInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 109)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2076)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TriggerInterface(PortInterface):
    """AUTOSAR TriggerInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    trigger_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize TriggerInterface."""
        super().__init__()
        self.trigger_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize TriggerInterface to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TriggerInterface, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize trigger_refs (list to container "TRIGGER-REFS")
        if self.trigger_refs:
            wrapper = ET.Element("TRIGGER-REFS")
            for item in self.trigger_refs:
                serialized = ARObject._serialize_item(item, "Trigger")
                if serialized is not None:
                    child_elem = ET.Element("TRIGGER-REF")
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
    def deserialize(cls, element: ET.Element) -> "TriggerInterface":
        """Deserialize XML element to TriggerInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TriggerInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TriggerInterface, cls).deserialize(element)

        # Parse trigger_refs (list from container "TRIGGER-REFS")
        obj.trigger_refs = []
        container = ARObject._find_child_element(element, "TRIGGER-REFS")
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
                    obj.trigger_refs.append(child_value)

        return obj



class TriggerInterfaceBuilder:
    """Builder for TriggerInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerInterface = TriggerInterface()

    def build(self) -> TriggerInterface:
        """Build and return TriggerInterface object.

        Returns:
            TriggerInterface instance
        """
        # TODO: Add validation
        return self._obj
