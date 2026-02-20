"""SomeipSdServerEventGroupTimingConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 517)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.request_response_delay import (
    RequestResponseDelay,
)


class SomeipSdServerEventGroupTimingConfig(ARElement):
    """AUTOSAR SomeipSdServerEventGroupTimingConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request: Optional[RequestResponseDelay]
    def __init__(self) -> None:
        """Initialize SomeipSdServerEventGroupTimingConfig."""
        super().__init__()
        self.request: Optional[RequestResponseDelay] = None

    def serialize(self) -> ET.Element:
        """Serialize SomeipSdServerEventGroupTimingConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SomeipSdServerEventGroupTimingConfig, self).serialize()

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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipSdServerEventGroupTimingConfig":
        """Deserialize XML element to SomeipSdServerEventGroupTimingConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipSdServerEventGroupTimingConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipSdServerEventGroupTimingConfig, cls).deserialize(element)

        # Parse request
        child = ARObject._find_child_element(element, "REQUEST")
        if child is not None:
            request_value = ARObject._deserialize_by_tag(child, "RequestResponseDelay")
            obj.request = request_value

        return obj



class SomeipSdServerEventGroupTimingConfigBuilder:
    """Builder for SomeipSdServerEventGroupTimingConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipSdServerEventGroupTimingConfig = SomeipSdServerEventGroupTimingConfig()

    def build(self) -> SomeipSdServerEventGroupTimingConfig:
        """Build and return SomeipSdServerEventGroupTimingConfig object.

        Returns:
            SomeipSdServerEventGroupTimingConfig instance
        """
        # TODO: Add validation
        return self._obj
