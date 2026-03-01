"""TDEventIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 66)

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
    TDEventIPduTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDEventIPdu(TDEventCom):
    """AUTOSAR TDEventIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-EVENT-I-PDU"


    i_pdu_ref: Optional[ARRef]
    physical_channel_ref: Optional[ARRef]
    td_event_type: Optional[TDEventIPduTypeEnum]
    _DESERIALIZE_DISPATCH = {
        "I-PDU-REF": ("_POLYMORPHIC", "i_pdu_ref", ["ContainerIPdu", "DcmIPdu", "GeneralPurposeIPdu", "ISignalIPdu", "J1939DcmIPdu", "MultiplexedIPdu", "NPdu", "SecuredIPdu", "UserDefinedIPdu"]),
        "PHYSICAL-CHANNEL-REF": ("_POLYMORPHIC", "physical_channel_ref", ["AbstractCanPhysicalChannel", "EthernetPhysicalChannel", "FlexrayPhysicalChannel", "LinPhysicalChannel"]),
        "TD-EVENT-TYPE": lambda obj, elem: setattr(obj, "td_event_type", TDEventIPduTypeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TDEventIPdu."""
        super().__init__()
        self.i_pdu_ref: Optional[ARRef] = None
        self.physical_channel_ref: Optional[ARRef] = None
        self.td_event_type: Optional[TDEventIPduTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_pdu_ref
        if self.i_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.i_pdu_ref, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-PDU-REF")
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

        # Serialize td_event_type
        if self.td_event_type is not None:
            serialized = SerializationHelper.serialize_item(self.td_event_type, "TDEventIPduTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventIPdu":
        """Deserialize XML element to TDEventIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventIPdu, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "I-PDU-REF":
                setattr(obj, "i_pdu_ref", ARRef.deserialize(child))
            elif tag == "PHYSICAL-CHANNEL-REF":
                setattr(obj, "physical_channel_ref", ARRef.deserialize(child))
            elif tag == "TD-EVENT-TYPE":
                setattr(obj, "td_event_type", TDEventIPduTypeEnum.deserialize(child))

        return obj



class TDEventIPduBuilder(TDEventComBuilder):
    """Builder for TDEventIPdu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventIPdu = TDEventIPdu()


    def with_i_pdu(self, value: Optional[IPdu]) -> "TDEventIPduBuilder":
        """Set i_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.i_pdu = value
        return self

    def with_physical_channel(self, value: Optional[PhysicalChannel]) -> "TDEventIPduBuilder":
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

    def with_td_event_type(self, value: Optional[TDEventIPduTypeEnum]) -> "TDEventIPduBuilder":
        """Set td_event_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.td_event_type = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> TDEventIPdu:
        """Build and return the TDEventIPdu instance with validation."""
        self._validate_instance()
        pass
        return self._obj