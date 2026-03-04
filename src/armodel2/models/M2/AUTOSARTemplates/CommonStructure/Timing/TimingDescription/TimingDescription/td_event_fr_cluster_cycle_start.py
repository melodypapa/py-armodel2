"""TDEventFrClusterCycleStart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 71)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_cycle_start import (
    TDEventCycleStart,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_cycle_start import TDEventCycleStartBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_cluster import (
    FlexrayCluster,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDEventFrClusterCycleStart(TDEventCycleStart):
    """AUTOSAR TDEventFrClusterCycleStart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-EVENT-FR-CLUSTER-CYCLE-START"


    fr_cluster_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "FR-CLUSTER-REF": lambda obj, elem: setattr(obj, "fr_cluster_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TDEventFrClusterCycleStart."""
        super().__init__()
        self.fr_cluster_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventFrClusterCycleStart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventFrClusterCycleStart, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize fr_cluster_ref
        if self.fr_cluster_ref is not None:
            serialized = SerializationHelper.serialize_item(self.fr_cluster_ref, "FlexrayCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FR-CLUSTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventFrClusterCycleStart":
        """Deserialize XML element to TDEventFrClusterCycleStart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventFrClusterCycleStart object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventFrClusterCycleStart, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FR-CLUSTER-REF":
                setattr(obj, "fr_cluster_ref", ARRef.deserialize(child))

        return obj



class TDEventFrClusterCycleStartBuilder(TDEventCycleStartBuilder):
    """Builder for TDEventFrClusterCycleStart with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventFrClusterCycleStart = TDEventFrClusterCycleStart()


    def with_fr_cluster(self, value: Optional[FlexrayCluster]) -> "TDEventFrClusterCycleStartBuilder":
        """Set fr_cluster attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.fr_cluster = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "frCluster",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TDEventFrClusterCycleStart:
        """Build and return the TDEventFrClusterCycleStart instance with validation."""
        self._validate_instance()
        return self._obj