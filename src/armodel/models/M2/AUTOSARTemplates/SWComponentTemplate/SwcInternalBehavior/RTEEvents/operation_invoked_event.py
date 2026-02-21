"""OperationInvokedEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 325)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 543)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class OperationInvokedEvent(RTEEvent):
    """AUTOSAR OperationInvokedEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operation_instance_ref: Optional[ClientServerOperation]
    def __init__(self) -> None:
        """Initialize OperationInvokedEvent."""
        super().__init__()
        self.operation_instance_ref: Optional[ClientServerOperation] = None

    def serialize(self) -> ET.Element:
        """Serialize OperationInvokedEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(OperationInvokedEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize operation_instance_ref
        if self.operation_instance_ref is not None:
            serialized = ARObject._serialize_item(self.operation_instance_ref, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPERATION-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "OperationInvokedEvent":
        """Deserialize XML element to OperationInvokedEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized OperationInvokedEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(OperationInvokedEvent, cls).deserialize(element)

        # Parse operation_instance_ref
        child = ARObject._find_child_element(element, "OPERATION-INSTANCE-REF")
        if child is not None:
            operation_instance_ref_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.operation_instance_ref = operation_instance_ref_value

        return obj



class OperationInvokedEventBuilder:
    """Builder for OperationInvokedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OperationInvokedEvent = OperationInvokedEvent()

    def build(self) -> OperationInvokedEvent:
        """Build and return OperationInvokedEvent object.

        Returns:
            OperationInvokedEvent instance
        """
        # TODO: Add validation
        return self._obj
