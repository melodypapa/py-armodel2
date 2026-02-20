"""TDEventVfbReference AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 52)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb import (
    TDEventVfb,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class TDEventVfbReference(TDEventVfb):
    """AUTOSAR TDEventVfbReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    referenced_td_event_vfb_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TDEventVfbReference."""
        super().__init__()
        self.referenced_td_event_vfb_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventVfbReference to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventVfbReference, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize referenced_td_event_vfb_ref
        if self.referenced_td_event_vfb_ref is not None:
            serialized = ARObject._serialize_item(self.referenced_td_event_vfb_ref, "TDEventVfb")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFERENCED-TD-EVENT-VFB-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventVfbReference":
        """Deserialize XML element to TDEventVfbReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventVfbReference object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventVfbReference, cls).deserialize(element)

        # Parse referenced_td_event_vfb_ref
        child = ARObject._find_child_element(element, "REFERENCED-TD-EVENT-VFB-REF")
        if child is not None:
            referenced_td_event_vfb_ref_value = ARRef.deserialize(child)
            obj.referenced_td_event_vfb_ref = referenced_td_event_vfb_ref_value

        return obj



class TDEventVfbReferenceBuilder:
    """Builder for TDEventVfbReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVfbReference = TDEventVfbReference()

    def build(self) -> TDEventVfbReference:
        """Build and return TDEventVfbReference object.

        Returns:
            TDEventVfbReference instance
        """
        # TODO: Add validation
        return self._obj
