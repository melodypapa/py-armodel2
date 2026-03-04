"""IEEE1722TpAcfLinPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 667)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import (
    IEEE1722TpAcfBusPart,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import IEEE1722TpAcfBusPartBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IEEE1722TpAcfLinPart(IEEE1722TpAcfBusPart):
    """AUTOSAR IEEE1722TpAcfLinPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-E-E-E1722-TP-ACF-LIN-PART"


    lin_identifier: Optional[PositiveInteger]
    sdu_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "LIN-IDENTIFIER": lambda obj, elem: setattr(obj, "lin_identifier", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SDU-REF": lambda obj, elem: setattr(obj, "sdu_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfLinPart."""
        super().__init__()
        self.lin_identifier: Optional[PositiveInteger] = None
        self.sdu_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAcfLinPart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAcfLinPart, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lin_identifier
        if self.lin_identifier is not None:
            serialized = SerializationHelper.serialize_item(self.lin_identifier, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIN-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdu_ref
        if self.sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sdu_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfLinPart":
        """Deserialize XML element to IEEE1722TpAcfLinPart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfLinPart object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAcfLinPart, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LIN-IDENTIFIER":
                setattr(obj, "lin_identifier", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SDU-REF":
                setattr(obj, "sdu_ref", ARRef.deserialize(child))

        return obj



class IEEE1722TpAcfLinPartBuilder(IEEE1722TpAcfBusPartBuilder):
    """Builder for IEEE1722TpAcfLinPart with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IEEE1722TpAcfLinPart = IEEE1722TpAcfLinPart()


    def with_lin_identifier(self, value: Optional[PositiveInteger]) -> "IEEE1722TpAcfLinPartBuilder":
        """Set lin_identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lin_identifier = value
        return self

    def with_sdu(self, value: Optional[PduTriggering]) -> "IEEE1722TpAcfLinPartBuilder":
        """Set sdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdu = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "linIdentifier",
        "sdu",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IEEE1722TpAcfLinPart:
        """Build and return the IEEE1722TpAcfLinPart instance with validation."""
        self._validate_instance()
        return self._obj