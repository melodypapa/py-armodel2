"""TDEventTTCanCycleStart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 72)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_cycle_start import (
    TDEventCycleStart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanTopology.ttcan_cluster import (
    TtcanCluster,
)


class TDEventTTCanCycleStart(TDEventCycleStart):
    """AUTOSAR TDEventTTCanCycleStart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tt_can_cluster_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TDEventTTCanCycleStart."""
        super().__init__()
        self.tt_can_cluster_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventTTCanCycleStart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventTTCanCycleStart, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tt_can_cluster_ref
        if self.tt_can_cluster_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tt_can_cluster_ref, "TtcanCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TT-CAN-CLUSTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventTTCanCycleStart":
        """Deserialize XML element to TDEventTTCanCycleStart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventTTCanCycleStart object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventTTCanCycleStart, cls).deserialize(element)

        # Parse tt_can_cluster_ref
        child = SerializationHelper.find_child_element(element, "TT-CAN-CLUSTER-REF")
        if child is not None:
            tt_can_cluster_ref_value = ARRef.deserialize(child)
            obj.tt_can_cluster_ref = tt_can_cluster_ref_value

        return obj



class TDEventTTCanCycleStartBuilder:
    """Builder for TDEventTTCanCycleStart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventTTCanCycleStart = TDEventTTCanCycleStart()

    def build(self) -> TDEventTTCanCycleStart:
        """Build and return TDEventTTCanCycleStart object.

        Returns:
            TDEventTTCanCycleStart instance
        """
        # TODO: Add validation
        return self._obj
