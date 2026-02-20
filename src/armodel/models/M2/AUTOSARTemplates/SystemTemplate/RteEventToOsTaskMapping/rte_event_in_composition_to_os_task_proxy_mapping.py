"""RteEventInCompositionToOsTaskProxyMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 211)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_RteEventToOsTaskMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.os_task_proxy import (
    OsTaskProxy,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class RteEventInCompositionToOsTaskProxyMapping(Identifiable):
    """AUTOSAR RteEventInCompositionToOsTaskProxyMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    offset: Optional[PositiveInteger]
    os_task_proxy_ref: Optional[ARRef]
    rte_event_instance_ref: Optional[RTEEvent]
    def __init__(self) -> None:
        """Initialize RteEventInCompositionToOsTaskProxyMapping."""
        super().__init__()
        self.offset: Optional[PositiveInteger] = None
        self.os_task_proxy_ref: Optional[ARRef] = None
        self.rte_event_instance_ref: Optional[RTEEvent] = None

    def serialize(self) -> ET.Element:
        """Serialize RteEventInCompositionToOsTaskProxyMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RteEventInCompositionToOsTaskProxyMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize offset
        if self.offset is not None:
            serialized = ARObject._serialize_item(self.offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize os_task_proxy_ref
        if self.os_task_proxy_ref is not None:
            serialized = ARObject._serialize_item(self.os_task_proxy_ref, "OsTaskProxy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OS-TASK-PROXY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rte_event_instance_ref
        if self.rte_event_instance_ref is not None:
            serialized = ARObject._serialize_item(self.rte_event_instance_ref, "RTEEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RTE-EVENT-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RteEventInCompositionToOsTaskProxyMapping":
        """Deserialize XML element to RteEventInCompositionToOsTaskProxyMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RteEventInCompositionToOsTaskProxyMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RteEventInCompositionToOsTaskProxyMapping, cls).deserialize(element)

        # Parse offset
        child = ARObject._find_child_element(element, "OFFSET")
        if child is not None:
            offset_value = child.text
            obj.offset = offset_value

        # Parse os_task_proxy_ref
        child = ARObject._find_child_element(element, "OS-TASK-PROXY-REF")
        if child is not None:
            os_task_proxy_ref_value = ARRef.deserialize(child)
            obj.os_task_proxy_ref = os_task_proxy_ref_value

        # Parse rte_event_instance_ref
        child = ARObject._find_child_element(element, "RTE-EVENT-INSTANCE-REF")
        if child is not None:
            rte_event_instance_ref_value = ARObject._deserialize_by_tag(child, "RTEEvent")
            obj.rte_event_instance_ref = rte_event_instance_ref_value

        return obj



class RteEventInCompositionToOsTaskProxyMappingBuilder:
    """Builder for RteEventInCompositionToOsTaskProxyMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RteEventInCompositionToOsTaskProxyMapping = RteEventInCompositionToOsTaskProxyMapping()

    def build(self) -> RteEventInCompositionToOsTaskProxyMapping:
        """Build and return RteEventInCompositionToOsTaskProxyMapping object.

        Returns:
            RteEventInCompositionToOsTaskProxyMapping instance
        """
        # TODO: Add validation
        return self._obj
