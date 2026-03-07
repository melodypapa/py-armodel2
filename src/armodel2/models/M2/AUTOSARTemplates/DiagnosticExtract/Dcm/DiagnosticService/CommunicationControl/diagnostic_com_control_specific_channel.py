"""DiagnosticComControlSpecificChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticComControlSpecificChannel(ARObject):
    """AUTOSAR DiagnosticComControlSpecificChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-COM-CONTROL-SPECIFIC-CHANNEL"


    specific_channel_ref: Optional[ARRef]
    specific_physical_ref: Optional[Any]
    subnet_number: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "SPECIFIC-CHANNEL-REF": ("_POLYMORPHIC", "specific_channel_ref", ["AbstractCanCluster", "CanCluster", "EthernetCluster", "FlexrayCluster", "J1939Cluster", "LinCluster", "TtcanCluster", "UserDefinedCluster"]),
        "SPECIFIC-PHYSICAL-REF": lambda obj, elem: setattr(obj, "specific_physical_ref", ARRef.deserialize(elem)),
        "SUBNET-NUMBER": lambda obj, elem: setattr(obj, "subnet_number", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticComControlSpecificChannel."""
        super().__init__()
        self.specific_channel_ref: Optional[ARRef] = None
        self.specific_physical_ref: Optional[Any] = None
        self.subnet_number: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticComControlSpecificChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticComControlSpecificChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize specific_channel_ref
        if self.specific_channel_ref is not None:
            serialized = SerializationHelper.serialize_item(self.specific_channel_ref, "CommunicationCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SPECIFIC-CHANNEL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize specific_physical_ref
        if self.specific_physical_ref is not None:
            serialized = SerializationHelper.serialize_item(self.specific_physical_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SPECIFIC-PHYSICAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize subnet_number
        if self.subnet_number is not None:
            serialized = SerializationHelper.serialize_item(self.subnet_number, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUBNET-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControlSpecificChannel":
        """Deserialize XML element to DiagnosticComControlSpecificChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticComControlSpecificChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticComControlSpecificChannel, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SPECIFIC-CHANNEL-REF":
                setattr(obj, "specific_channel_ref", ARRef.deserialize(child))
            elif tag == "SPECIFIC-PHYSICAL-REF":
                setattr(obj, "specific_physical_ref", ARRef.deserialize(child))
            elif tag == "SUBNET-NUMBER":
                setattr(obj, "subnet_number", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DiagnosticComControlSpecificChannelBuilder(BuilderBase):
    """Builder for DiagnosticComControlSpecificChannel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticComControlSpecificChannel = DiagnosticComControlSpecificChannel()


    def with_specific_channel(self, value: Optional[CommunicationCluster]) -> "DiagnosticComControlSpecificChannelBuilder":
        """Set specific_channel attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'specific_channel' is required and cannot be None")
        self._obj.specific_channel = value
        return self

    def with_specific_physical(self, value: Optional[Any]) -> "DiagnosticComControlSpecificChannelBuilder":
        """Set specific_physical attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'specific_physical' is required and cannot be None")
        self._obj.specific_physical = value
        return self

    def with_subnet_number(self, value: Optional[PositiveInteger]) -> "DiagnosticComControlSpecificChannelBuilder":
        """Set subnet_number attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'subnet_number' is required and cannot be None")
        self._obj.subnet_number = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "specificChannel",
        "specificPhysical",
        "subnetNumber",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticComControlSpecificChannel:
        """Build and return the DiagnosticComControlSpecificChannel instance with validation."""
        self._validate_instance()
        return self._obj