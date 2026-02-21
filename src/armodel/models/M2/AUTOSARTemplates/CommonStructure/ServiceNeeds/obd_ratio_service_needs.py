"""ObdRatioServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 795)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ObdRatioConnectionKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_needs import (
    DiagnosticEventNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)


class ObdRatioServiceNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdRatioServiceNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connection_type: Optional[ObdRatioConnectionKindEnum]
    rate_based_monitored_event_ref: Optional[ARRef]
    used_fid_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ObdRatioServiceNeeds."""
        super().__init__()
        self.connection_type: Optional[ObdRatioConnectionKindEnum] = None
        self.rate_based_monitored_event_ref: Optional[ARRef] = None
        self.used_fid_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ObdRatioServiceNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ObdRatioServiceNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connection_type
        if self.connection_type is not None:
            serialized = ARObject._serialize_item(self.connection_type, "ObdRatioConnectionKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONNECTION-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rate_based_monitored_event_ref
        if self.rate_based_monitored_event_ref is not None:
            serialized = ARObject._serialize_item(self.rate_based_monitored_event_ref, "DiagnosticEventNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATE-BASED-MONITORED-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize used_fid_ref
        if self.used_fid_ref is not None:
            serialized = ARObject._serialize_item(self.used_fid_ref, "FunctionInhibitionNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-FID-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ObdRatioServiceNeeds":
        """Deserialize XML element to ObdRatioServiceNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ObdRatioServiceNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ObdRatioServiceNeeds, cls).deserialize(element)

        # Parse connection_type
        child = ARObject._find_child_element(element, "CONNECTION-TYPE")
        if child is not None:
            connection_type_value = ObdRatioConnectionKindEnum.deserialize(child)
            obj.connection_type = connection_type_value

        # Parse rate_based_monitored_event_ref
        child = ARObject._find_child_element(element, "RATE-BASED-MONITORED-EVENT-REF")
        if child is not None:
            rate_based_monitored_event_ref_value = ARRef.deserialize(child)
            obj.rate_based_monitored_event_ref = rate_based_monitored_event_ref_value

        # Parse used_fid_ref
        child = ARObject._find_child_element(element, "USED-FID-REF")
        if child is not None:
            used_fid_ref_value = ARRef.deserialize(child)
            obj.used_fid_ref = used_fid_ref_value

        return obj



class ObdRatioServiceNeedsBuilder:
    """Builder for ObdRatioServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ObdRatioServiceNeeds = ObdRatioServiceNeeds()

    def build(self) -> ObdRatioServiceNeeds:
        """Build and return ObdRatioServiceNeeds object.

        Returns:
            ObdRatioServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
