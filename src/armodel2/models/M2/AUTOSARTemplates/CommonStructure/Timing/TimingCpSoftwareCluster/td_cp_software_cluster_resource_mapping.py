"""TDCpSoftwareClusterResourceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCpSoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDCpSoftwareClusterResourceMapping(Identifiable):
    """AUTOSAR TDCpSoftwareClusterResourceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-CP-SOFTWARE-CLUSTER-RESOURCE-MAPPING"


    resource_ref: Optional[ARRef]
    timing_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "RESOURCE-REF": lambda obj, elem: setattr(obj, "resource_ref", ARRef.deserialize(elem)),
        "TIMING-REF": ("_POLYMORPHIC", "timing_ref", ["TDEventBswInternalBehavior", "TDEventBswModeDeclaration", "TDEventBswModule", "TDEventComplex", "TDEventFrClusterCycleStart", "TDEventFrame", "TDEventFrameEthernet", "TDEventIPdu", "TDEventISignal", "TDEventModeDeclaration", "TDEventOperation", "TDEventSLLETPort", "TDEventSwcInternalBehavior", "TDEventSwcInternalBehaviorReference", "TDEventTTCanCycleStart", "TDEventTrigger", "TDEventVariableDataPrototype", "TDEventVfbReference", "TimingDescriptionEvent", "TimingDescriptionEventChain"]),
    }


    def __init__(self) -> None:
        """Initialize TDCpSoftwareClusterResourceMapping."""
        super().__init__()
        self.resource_ref: Optional[ARRef] = None
        self.timing_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TDCpSoftwareClusterResourceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDCpSoftwareClusterResourceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize resource_ref
        if self.resource_ref is not None:
            serialized = SerializationHelper.serialize_item(self.resource_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESOURCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_ref
        if self.timing_ref is not None:
            serialized = SerializationHelper.serialize_item(self.timing_ref, "TimingDescription")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDCpSoftwareClusterResourceMapping":
        """Deserialize XML element to TDCpSoftwareClusterResourceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDCpSoftwareClusterResourceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDCpSoftwareClusterResourceMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RESOURCE-REF":
                setattr(obj, "resource_ref", ARRef.deserialize(child))
            elif tag == "TIMING-REF":
                setattr(obj, "timing_ref", ARRef.deserialize(child))

        return obj



class TDCpSoftwareClusterResourceMappingBuilder(IdentifiableBuilder):
    """Builder for TDCpSoftwareClusterResourceMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDCpSoftwareClusterResourceMapping = TDCpSoftwareClusterResourceMapping()


    def with_resource(self, value: Optional[CpSoftwareCluster]) -> "TDCpSoftwareClusterResourceMappingBuilder":
        """Set resource attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'resource' is required and cannot be None")
        self._obj.resource = value
        return self

    def with_timing(self, value: Optional[TimingDescription]) -> "TDCpSoftwareClusterResourceMappingBuilder":
        """Set timing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'timing' is required and cannot be None")
        self._obj.timing = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "resource",
        "timing",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TDCpSoftwareClusterResourceMapping:
        """Build and return the TDCpSoftwareClusterResourceMapping instance with validation."""
        self._validate_instance()
        return self._obj