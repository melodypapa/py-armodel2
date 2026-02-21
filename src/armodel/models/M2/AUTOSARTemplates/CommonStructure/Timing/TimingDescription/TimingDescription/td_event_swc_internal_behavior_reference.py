"""TDEventSwcInternalBehaviorReference AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_swc import (
    TDEventSwc,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class TDEventSwcInternalBehaviorReference(TDEventSwc):
    """AUTOSAR TDEventSwcInternalBehaviorReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    referenced_td_event_swc_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TDEventSwcInternalBehaviorReference."""
        super().__init__()
        self.referenced_td_event_swc_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventSwcInternalBehaviorReference to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventSwcInternalBehaviorReference, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize referenced_td_event_swc_ref
        if self.referenced_td_event_swc_ref is not None:
            serialized = SerializationHelper.serialize_item(self.referenced_td_event_swc_ref, "TDEventSwc")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFERENCED-TD-EVENT-SWC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventSwcInternalBehaviorReference":
        """Deserialize XML element to TDEventSwcInternalBehaviorReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventSwcInternalBehaviorReference object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventSwcInternalBehaviorReference, cls).deserialize(element)

        # Parse referenced_td_event_swc_ref
        child = SerializationHelper.find_child_element(element, "REFERENCED-TD-EVENT-SWC-REF")
        if child is not None:
            referenced_td_event_swc_ref_value = ARRef.deserialize(child)
            obj.referenced_td_event_swc_ref = referenced_td_event_swc_ref_value

        return obj



class TDEventSwcInternalBehaviorReferenceBuilder:
    """Builder for TDEventSwcInternalBehaviorReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventSwcInternalBehaviorReference = TDEventSwcInternalBehaviorReference()

    def build(self) -> TDEventSwcInternalBehaviorReference:
        """Build and return TDEventSwcInternalBehaviorReference object.

        Returns:
            TDEventSwcInternalBehaviorReference instance
        """
        # TODO: Add validation
        return self._obj
