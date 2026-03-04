"""DoIpTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 555)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DiagnosticConnection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import TpConnectionBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DoIpTpConnection(TpConnection):
    """AUTOSAR DoIpTpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DO-IP-TP-CONNECTION"


    do_ip_source_ref: Optional[ARRef]
    do_ip_target_ref: Optional[ARRef]
    tp_sdu_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DO-IP-SOURCE-REF": lambda obj, elem: setattr(obj, "do_ip_source_ref", ARRef.deserialize(elem)),
        "DO-IP-TARGET-REF": lambda obj, elem: setattr(obj, "do_ip_target_ref", ARRef.deserialize(elem)),
        "TP-SDU-REF": lambda obj, elem: setattr(obj, "tp_sdu_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DoIpTpConnection."""
        super().__init__()
        self.do_ip_source_ref: Optional[ARRef] = None
        self.do_ip_target_ref: Optional[ARRef] = None
        self.tp_sdu_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DoIpTpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DoIpTpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize do_ip_source_ref
        if self.do_ip_source_ref is not None:
            serialized = SerializationHelper.serialize_item(self.do_ip_source_ref, "DoIpLogicAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DO-IP-SOURCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize do_ip_target_ref
        if self.do_ip_target_ref is not None:
            serialized = SerializationHelper.serialize_item(self.do_ip_target_ref, "DoIpLogicAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DO-IP-TARGET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_sdu_ref
        if self.tp_sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tp_sdu_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-SDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpTpConnection":
        """Deserialize XML element to DoIpTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpTpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpTpConnection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DO-IP-SOURCE-REF":
                setattr(obj, "do_ip_source_ref", ARRef.deserialize(child))
            elif tag == "DO-IP-TARGET-REF":
                setattr(obj, "do_ip_target_ref", ARRef.deserialize(child))
            elif tag == "TP-SDU-REF":
                setattr(obj, "tp_sdu_ref", ARRef.deserialize(child))

        return obj



class DoIpTpConnectionBuilder(TpConnectionBuilder):
    """Builder for DoIpTpConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DoIpTpConnection = DoIpTpConnection()


    def with_do_ip_source(self, value: Optional[DoIpLogicAddress]) -> "DoIpTpConnectionBuilder":
        """Set do_ip_source attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.do_ip_source = value
        return self

    def with_do_ip_target(self, value: Optional[DoIpLogicAddress]) -> "DoIpTpConnectionBuilder":
        """Set do_ip_target attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.do_ip_target = value
        return self

    def with_tp_sdu(self, value: Optional[PduTriggering]) -> "DoIpTpConnectionBuilder":
        """Set tp_sdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tp_sdu = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "doIpSource",
        "doIpTarget",
        "tpSdu",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DoIpTpConnection:
        """Build and return the DoIpTpConnection instance with validation."""
        self._validate_instance()
        return self._obj