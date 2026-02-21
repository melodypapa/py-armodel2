"""PduTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 303)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 348)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 234)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu_port import (
    IPduPort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.sec_oc_crypto_service_mapping import (
    SecOcCryptoServiceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.trigger_i_pdu_send_condition import (
    TriggerIPduSendCondition,
)


class PduTriggering(Identifiable):
    """AUTOSAR PduTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu_ref: Optional[ARRef]
    i_pdu_port_refs: list[ARRef]
    i_signal_refs: list[ARRef]
    sec_oc_crypto_service_ref: Optional[ARRef]
    trigger_i_pdu_send_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PduTriggering."""
        super().__init__()
        self.i_pdu_ref: Optional[ARRef] = None
        self.i_pdu_port_refs: list[ARRef] = []
        self.i_signal_refs: list[ARRef] = []
        self.sec_oc_crypto_service_ref: Optional[ARRef] = None
        self.trigger_i_pdu_send_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PduTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse i_pdu_ref
        child = SerializationHelper.find_child_element(element, "I-PDU-REF")
        if child is not None:
            i_pdu_ref_value = ARRef.deserialize(child)
            obj.i_pdu_ref = i_pdu_ref_value

        # Parse i_pdu_port_refs (list from container "I-PDU-PORT-REFS")
        obj.i_pdu_port_refs = []
        container = SerializationHelper.find_child_element(element, "I-PDU-PORT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_pdu_port_refs.append(child_value)

        # Parse i_signal_refs (list from container "I-SIGNAL-REFS")
        obj.i_signal_refs = []
        container = SerializationHelper.find_child_element(element, "I-SIGNAL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_signal_refs.append(child_value)

        # Parse sec_oc_crypto_service_ref
        child = SerializationHelper.find_child_element(element, "SEC-OC-CRYPTO-SERVICE-REF")
        if child is not None:
            sec_oc_crypto_service_ref_value = ARRef.deserialize(child)
            obj.sec_oc_crypto_service_ref = sec_oc_crypto_service_ref_value

        # Parse trigger_i_pdu_send_refs (list from container "TRIGGER-I-PDU-SEND-REFS")
        obj.trigger_i_pdu_send_refs = []
        container = SerializationHelper.find_child_element(element, "TRIGGER-I-PDU-SEND-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.trigger_i_pdu_send_refs.append(child_value)

        return obj



class PduTriggeringBuilder:
    """Builder for PduTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PduTriggering = PduTriggering()

    def build(self) -> PduTriggering:
        """Build and return PduTriggering object.

        Returns:
            PduTriggering instance
        """
        # TODO: Add validation
        return self._obj
