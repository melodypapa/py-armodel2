"""J1939TpPg AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 625)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class J1939TpPg(ARObject):
    """AUTOSAR J1939TpPg."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "J1939-TP-PG"


    direct_pdu_ref: Optional[ARRef]
    pgn: Optional[Integer]
    requestable: Optional[Boolean]
    sdu_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DIRECT-PDU-REF": lambda obj, elem: setattr(obj, "direct_pdu_ref", ARRef.deserialize(elem)),
        "PGN": lambda obj, elem: setattr(obj, "pgn", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "REQUESTABLE": lambda obj, elem: setattr(obj, "requestable", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "SDU-REFS": ("_POLYMORPHIC_LIST", "sdu_refs", ["ContainerIPdu", "DcmIPdu", "GeneralPurposeIPdu", "ISignalIPdu", "J1939DcmIPdu", "MultiplexedIPdu", "NPdu", "SecuredIPdu", "UserDefinedIPdu"]),
    }


    def __init__(self) -> None:
        """Initialize J1939TpPg."""
        super().__init__()
        self.direct_pdu_ref: Optional[ARRef] = None
        self.pgn: Optional[Integer] = None
        self.requestable: Optional[Boolean] = None
        self.sdu_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize J1939TpPg to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939TpPg, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize direct_pdu_ref
        if self.direct_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.direct_pdu_ref, "NPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIRECT-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pgn
        if self.pgn is not None:
            serialized = SerializationHelper.serialize_item(self.pgn, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PGN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize requestable
        if self.requestable is not None:
            serialized = SerializationHelper.serialize_item(self.requestable, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUESTABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdu_refs (list to container "SDU-REFS")
        if self.sdu_refs:
            wrapper = ET.Element("SDU-REFS")
            for item in self.sdu_refs:
                serialized = SerializationHelper.serialize_item(item, "IPdu")
                if serialized is not None:
                    child_elem = ET.Element("SDU-REF")
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
    def deserialize(cls, element: ET.Element) -> "J1939TpPg":
        """Deserialize XML element to J1939TpPg object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939TpPg object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939TpPg, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DIRECT-PDU-REF":
                setattr(obj, "direct_pdu_ref", ARRef.deserialize(child))
            elif tag == "PGN":
                setattr(obj, "pgn", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "REQUESTABLE":
                setattr(obj, "requestable", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "SDU-REFS":
                for item_elem in child:
                    obj.sdu_refs.append(ARRef.deserialize(item_elem))

        return obj



class J1939TpPgBuilder(BuilderBase):
    """Builder for J1939TpPg with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: J1939TpPg = J1939TpPg()


    def with_direct_pdu(self, value: Optional[NPdu]) -> "J1939TpPgBuilder":
        """Set direct_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'direct_pdu' is required and cannot be None")
        self._obj.direct_pdu = value
        return self

    def with_pgn(self, value: Optional[Integer]) -> "J1939TpPgBuilder":
        """Set pgn attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'pgn' is required and cannot be None")
        self._obj.pgn = value
        return self

    def with_requestable(self, value: Optional[Boolean]) -> "J1939TpPgBuilder":
        """Set requestable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'requestable' is required and cannot be None")
        self._obj.requestable = value
        return self

    def with_sdus(self, items: list[IPdu]) -> "J1939TpPgBuilder":
        """Set sdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sdus = list(items) if items else []
        return self


    def add_sdu(self, item: IPdu) -> "J1939TpPgBuilder":
        """Add a single item to sdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sdus.append(item)
        return self

    def clear_sdus(self) -> "J1939TpPgBuilder":
        """Clear all items from sdus list.

        Returns:
            self for method chaining
        """
        self._obj.sdus = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "directPdu",
        "pgn",
        "requestable",
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


    def build(self) -> J1939TpPg:
        """Build and return the J1939TpPg instance with validation."""
        self._validate_instance()
        return self._obj