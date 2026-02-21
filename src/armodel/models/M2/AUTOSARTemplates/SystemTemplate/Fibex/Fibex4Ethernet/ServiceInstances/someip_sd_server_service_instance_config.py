"""SomeipSdServerServiceInstanceConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 513)

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
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.initial_sd_delay_config import (
    InitialSdDelayConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.request_response_delay import (
    RequestResponseDelay,
)


class SomeipSdServerServiceInstanceConfig(ARElement):
    """AUTOSAR SomeipSdServerServiceInstanceConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    initial_offer_behavior: Optional[InitialSdDelayConfig]
    offer_cyclic_delay: Optional[TimeValue]
    priority: Optional[PositiveInteger]
    request: Optional[RequestResponseDelay]
    service_offer: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SomeipSdServerServiceInstanceConfig."""
        super().__init__()
        self.initial_offer_behavior: Optional[InitialSdDelayConfig] = None
        self.offer_cyclic_delay: Optional[TimeValue] = None
        self.priority: Optional[PositiveInteger] = None
        self.request: Optional[RequestResponseDelay] = None
        self.service_offer: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SomeipSdServerServiceInstanceConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SomeipSdServerServiceInstanceConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize initial_offer_behavior
        if self.initial_offer_behavior is not None:
            serialized = ARObject._serialize_item(self.initial_offer_behavior, "InitialSdDelayConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-OFFER-BEHAVIOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize offer_cyclic_delay
        if self.offer_cyclic_delay is not None:
            serialized = ARObject._serialize_item(self.offer_cyclic_delay, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFER-CYCLIC-DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize priority
        if self.priority is not None:
            serialized = ARObject._serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize service_offer
        if self.service_offer is not None:
            serialized = ARObject._serialize_item(self.service_offer, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-OFFER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipSdServerServiceInstanceConfig":
        """Deserialize XML element to SomeipSdServerServiceInstanceConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipSdServerServiceInstanceConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipSdServerServiceInstanceConfig, cls).deserialize(element)

        # Parse initial_offer_behavior
        child = ARObject._find_child_element(element, "INITIAL-OFFER-BEHAVIOR")
        if child is not None:
            initial_offer_behavior_value = ARObject._deserialize_by_tag(child, "InitialSdDelayConfig")
            obj.initial_offer_behavior = initial_offer_behavior_value

        # Parse offer_cyclic_delay
        child = ARObject._find_child_element(element, "OFFER-CYCLIC-DELAY")
        if child is not None:
            offer_cyclic_delay_value = child.text
            obj.offer_cyclic_delay = offer_cyclic_delay_value

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse request
        child = ARObject._find_child_element(element, "REQUEST")
        if child is not None:
            request_value = ARObject._deserialize_by_tag(child, "RequestResponseDelay")
            obj.request = request_value

        # Parse service_offer
        child = ARObject._find_child_element(element, "SERVICE-OFFER")
        if child is not None:
            service_offer_value = child.text
            obj.service_offer = service_offer_value

        return obj



class SomeipSdServerServiceInstanceConfigBuilder:
    """Builder for SomeipSdServerServiceInstanceConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipSdServerServiceInstanceConfig = SomeipSdServerServiceInstanceConfig()

    def build(self) -> SomeipSdServerServiceInstanceConfig:
        """Build and return SomeipSdServerServiceInstanceConfig object.

        Returns:
            SomeipSdServerServiceInstanceConfig instance
        """
        # TODO: Add validation
        return self._obj
