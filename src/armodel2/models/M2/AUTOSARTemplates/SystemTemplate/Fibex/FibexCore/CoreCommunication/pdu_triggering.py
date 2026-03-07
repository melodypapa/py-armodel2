"""PduTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 303)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 348)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 234)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu_port import (
    IPduPort,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.sec_oc_crypto_service_mapping import (
    SecOcCryptoServiceMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.trigger_i_pdu_send_condition import (
    TriggerIPduSendCondition,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PduTriggering(Identifiable):
    """AUTOSAR PduTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PDU-TRIGGERING"


    i_pdu_port_refs: list[ARRef]
    i_pdu_ref: Optional[ARRef]
    i_signal_refs: list[ARRef]
    sec_oc_crypto_service_ref: Optional[ARRef]
    trigger_i_pdu_send_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "I-PDU-PORT-REFS": lambda obj, elem: [obj.i_pdu_port_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "I-PDU-REF": ("_POLYMORPHIC", "i_pdu_ref", ["ContainerIPdu", "DcmIPdu", "GeneralPurposeIPdu", "GeneralPurposePdu", "IPdu", "ISignalIPdu", "J1939DcmIPdu", "MultiplexedIPdu", "NPdu", "NmPdu", "SecuredIPdu", "UserDefinedIPdu", "UserDefinedPdu"]),
        "I-SIGNAL-REFS": lambda obj, elem: [obj.i_signal_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "SEC-OC-CRYPTO-SERVICE-REF": lambda obj, elem: setattr(obj, "sec_oc_crypto_service_ref", ARRef.deserialize(elem)),
        "TRIGGER-I-PDU-SEND-REFS": lambda obj, elem: [obj.trigger_i_pdu_send_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize PduTriggering."""
        super().__init__()
        self.i_pdu_port_refs: list[ARRef] = []
        self.i_pdu_ref: Optional[ARRef] = None
        self.i_signal_refs: list[ARRef] = []
        self.sec_oc_crypto_service_ref: Optional[ARRef] = None
        self.trigger_i_pdu_send_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PduTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PduTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_pdu_port_refs (list to container "I-PDU-PORT-REFS")
        if self.i_pdu_port_refs:
            wrapper = ET.Element("I-PDU-PORT-REFS")
            for item in self.i_pdu_port_refs:
                serialized = SerializationHelper.serialize_item(item, "IPduPort")
                if serialized is not None:
                    child_elem = ET.Element("I-PDU-PORT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize i_pdu_ref
        if self.i_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.i_pdu_ref, "Pdu")
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

        # Serialize i_signal_refs (list to container "I-SIGNAL-REFS")
        if self.i_signal_refs:
            wrapper = ET.Element("I-SIGNAL-REFS")
            for item in self.i_signal_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignalTriggering")
                if serialized is not None:
                    child_elem = ET.Element("I-SIGNAL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sec_oc_crypto_service_ref
        if self.sec_oc_crypto_service_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sec_oc_crypto_service_ref, "SecOcCryptoServiceMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEC-OC-CRYPTO-SERVICE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger_i_pdu_send_refs (list to container "TRIGGER-I-PDU-SEND-REFS")
        if self.trigger_i_pdu_send_refs:
            wrapper = ET.Element("TRIGGER-I-PDU-SEND-REFS")
            for item in self.trigger_i_pdu_send_refs:
                serialized = SerializationHelper.serialize_item(item, "TriggerIPduSendCondition")
                if serialized is not None:
                    child_elem = ET.Element("TRIGGER-I-PDU-SEND-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PduTriggering":
        """Deserialize XML element to PduTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PduTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PduTriggering, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "I-PDU-PORT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.i_pdu_port_refs.append(ARRef.deserialize(item_elem))
            elif tag == "I-PDU-REF":
                setattr(obj, "i_pdu_ref", ARRef.deserialize(child))
            elif tag == "I-SIGNAL-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.i_signal_refs.append(ARRef.deserialize(item_elem))
            elif tag == "SEC-OC-CRYPTO-SERVICE-REF":
                setattr(obj, "sec_oc_crypto_service_ref", ARRef.deserialize(child))
            elif tag == "TRIGGER-I-PDU-SEND-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.trigger_i_pdu_send_refs.append(ARRef.deserialize(item_elem))

        return obj



class PduTriggeringBuilder(IdentifiableBuilder):
    """Builder for PduTriggering with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PduTriggering = PduTriggering()


    def with_i_pdu_ports(self, items: list[IPduPort]) -> "PduTriggeringBuilder":
        """Set i_pdu_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_ports = list(items) if items else []
        return self

    def with_i_pdu(self, value: Optional[Pdu]) -> "PduTriggeringBuilder":
        """Set i_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'i_pdu' is required and cannot be None")
        self._obj.i_pdu = value
        return self

    def with_i_signals(self, items: list[ISignalTriggering]) -> "PduTriggeringBuilder":
        """Set i_signals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_signals = list(items) if items else []
        return self

    def with_sec_oc_crypto_service(self, value: Optional[SecOcCryptoServiceMapping]) -> "PduTriggeringBuilder":
        """Set sec_oc_crypto_service attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sec_oc_crypto_service' is required and cannot be None")
        self._obj.sec_oc_crypto_service = value
        return self

    def with_trigger_i_pdu_sends(self, items: list[TriggerIPduSendCondition]) -> "PduTriggeringBuilder":
        """Set trigger_i_pdu_sends list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.trigger_i_pdu_sends = list(items) if items else []
        return self


    def add_i_pdu_port(self, item: IPduPort) -> "PduTriggeringBuilder":
        """Add a single item to i_pdu_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_ports.append(item)
        return self

    def clear_i_pdu_ports(self) -> "PduTriggeringBuilder":
        """Clear all items from i_pdu_ports list.

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_ports = []
        return self

    def add_i_signal(self, item: ISignalTriggering) -> "PduTriggeringBuilder":
        """Add a single item to i_signals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_signals.append(item)
        return self

    def clear_i_signals(self) -> "PduTriggeringBuilder":
        """Clear all items from i_signals list.

        Returns:
            self for method chaining
        """
        self._obj.i_signals = []
        return self

    def add_trigger_i_pdu_send(self, item: TriggerIPduSendCondition) -> "PduTriggeringBuilder":
        """Add a single item to trigger_i_pdu_sends list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.trigger_i_pdu_sends.append(item)
        return self

    def clear_trigger_i_pdu_sends(self) -> "PduTriggeringBuilder":
        """Clear all items from trigger_i_pdu_sends list.

        Returns:
            self for method chaining
        """
        self._obj.trigger_i_pdu_sends = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "iPdu",
        "iPduPort",
        "iSignal",
        "secOcCryptoService",
        "triggerIPduSend",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PduTriggering:
        """Build and return the PduTriggering instance with validation."""
        self._validate_instance()
        return self._obj