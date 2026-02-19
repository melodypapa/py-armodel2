"""SomeipSdClientEventGroupTimingConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 521)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.request_response_delay import (
    RequestResponseDelay,
)


class SomeipSdClientEventGroupTimingConfig(ARElement):
    """AUTOSAR SomeipSdClientEventGroupTimingConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request: Optional[RequestResponseDelay]
    subscribe: Optional[PositiveInteger]
    time_to_live: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SomeipSdClientEventGroupTimingConfig."""
        super().__init__()
        self.request: Optional[RequestResponseDelay] = None
        self.subscribe: Optional[PositiveInteger] = None
        self.time_to_live: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize SomeipSdClientEventGroupTimingConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SomeipSdClientEventGroupTimingConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize request
        if self.request is not None:
            serialized = ARObject._serialize_item(self.request, "RequestResponseDelay")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize subscribe
        if self.subscribe is not None:
            serialized = ARObject._serialize_item(self.subscribe, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUBSCRIBE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_to_live
        if self.time_to_live is not None:
            serialized = ARObject._serialize_item(self.time_to_live, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-TO-LIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipSdClientEventGroupTimingConfig":
        """Deserialize XML element to SomeipSdClientEventGroupTimingConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipSdClientEventGroupTimingConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipSdClientEventGroupTimingConfig, cls).deserialize(element)

        # Parse request
        child = ARObject._find_child_element(element, "REQUEST")
        if child is not None:
            request_value = ARObject._deserialize_by_tag(child, "RequestResponseDelay")
            obj.request = request_value

        # Parse subscribe
        child = ARObject._find_child_element(element, "SUBSCRIBE")
        if child is not None:
            subscribe_value = child.text
            obj.subscribe = subscribe_value

        # Parse time_to_live
        child = ARObject._find_child_element(element, "TIME-TO-LIVE")
        if child is not None:
            time_to_live_value = child.text
            obj.time_to_live = time_to_live_value

        return obj



class SomeipSdClientEventGroupTimingConfigBuilder:
    """Builder for SomeipSdClientEventGroupTimingConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipSdClientEventGroupTimingConfig = SomeipSdClientEventGroupTimingConfig()

    def build(self) -> SomeipSdClientEventGroupTimingConfig:
        """Build and return SomeipSdClientEventGroupTimingConfig object.

        Returns:
            SomeipSdClientEventGroupTimingConfig instance
        """
        # TODO: Add validation
        return self._obj
