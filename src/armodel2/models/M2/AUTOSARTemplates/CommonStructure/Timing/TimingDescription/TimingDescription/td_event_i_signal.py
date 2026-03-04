"""TDEventISignal AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 65)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import TDEventComBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import (
    TDEventISignalTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDEventISignal(TDEventCom):
    """AUTOSAR TDEventISignal."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-EVENT-I-SIGNAL"


    i_signal_ref: Optional[ARRef]
    physical_channel_ref: Optional[ARRef]
    td_event_type_enum: Optional[TDEventISignalTypeEnum]
    _DESERIALIZE_DISPATCH = {
        "I-SIGNAL-REF": lambda obj, elem: setattr(obj, "i_signal_ref", ARRef.deserialize(elem)),
        "PHYSICAL-CHANNEL-REF": ("_POLYMORPHIC", "physical_channel_ref", ["AbstractCanPhysicalChannel", "CanPhysicalChannel", "EthernetPhysicalChannel", "FlexrayPhysicalChannel", "LinPhysicalChannel", "TtcanPhysicalChannel"]),
        "TD-EVENT-TYPE-ENUM": lambda obj, elem: setattr(obj, "td_event_type_enum", TDEventISignalTypeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TDEventISignal."""
        super().__init__()
        self.i_signal_ref: Optional[ARRef] = None
        self.physical_channel_ref: Optional[ARRef] = None
        self.td_event_type_enum: Optional[TDEventISignalTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventISignal to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventISignal, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_signal_ref
        if self.i_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.i_signal_ref, "ISignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize physical_channel_ref
        if self.physical_channel_ref is not None:
            serialized = SerializationHelper.serialize_item(self.physical_channel_ref, "PhysicalChannel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYSICAL-CHANNEL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event_type_enum
        if self.td_event_type_enum is not None:
            serialized = SerializationHelper.serialize_item(self.td_event_type_enum, "TDEventISignalTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-TYPE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventISignal":
        """Deserialize XML element to TDEventISignal object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventISignal object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventISignal, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "I-SIGNAL-REF":
                setattr(obj, "i_signal_ref", ARRef.deserialize(child))
            elif tag == "PHYSICAL-CHANNEL-REF":
                setattr(obj, "physical_channel_ref", ARRef.deserialize(child))
            elif tag == "TD-EVENT-TYPE-ENUM":
                setattr(obj, "td_event_type_enum", TDEventISignalTypeEnum.deserialize(child))

        return obj



class TDEventISignalBuilder(TDEventComBuilder):
    """Builder for TDEventISignal with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventISignal = TDEventISignal()


    def with_i_signal(self, value: Optional[ISignal]) -> "TDEventISignalBuilder":
        """Set i_signal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.i_signal = value
        return self

    def with_physical_channel(self, value: Optional[PhysicalChannel]) -> "TDEventISignalBuilder":
        """Set physical_channel attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.physical_channel = value
        return self

    def with_td_event_type_enum(self, value: Optional[TDEventISignalTypeEnum]) -> "TDEventISignalBuilder":
        """Set td_event_type_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.td_event_type_enum = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "iSignal",
        "physicalChannel",
        "tdEventTypeEnum",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TDEventISignal:
        """Build and return the TDEventISignal instance with validation."""
        self._validate_instance()
        return self._obj