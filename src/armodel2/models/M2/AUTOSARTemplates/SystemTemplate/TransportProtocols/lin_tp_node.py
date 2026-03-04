"""LinTpNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 614)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LinTpNode(Identifiable):
    """AUTOSAR LinTpNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LIN-TP-NODE"


    connector_ref: Optional[Any]
    drop_not: Optional[Boolean]
    max_number_of: Optional[Integer]
    p2_max: Optional[TimeValue]
    p2_timing: Optional[TimeValue]
    tp_address_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONNECTOR-REF": lambda obj, elem: setattr(obj, "connector_ref", ARRef.deserialize(elem)),
        "DROP-NOT": lambda obj, elem: setattr(obj, "drop_not", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "MAX-NUMBER-OF": lambda obj, elem: setattr(obj, "max_number_of", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "P2-MAX": lambda obj, elem: setattr(obj, "p2_max", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "P2-TIMING": lambda obj, elem: setattr(obj, "p2_timing", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TP-ADDRESS-REF": lambda obj, elem: setattr(obj, "tp_address_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize LinTpNode."""
        super().__init__()
        self.connector_ref: Optional[Any] = None
        self.drop_not: Optional[Boolean] = None
        self.max_number_of: Optional[Integer] = None
        self.p2_max: Optional[TimeValue] = None
        self.p2_timing: Optional[TimeValue] = None
        self.tp_address_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize LinTpNode to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinTpNode, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connector_ref
        if self.connector_ref is not None:
            serialized = SerializationHelper.serialize_item(self.connector_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONNECTOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize drop_not
        if self.drop_not is not None:
            serialized = SerializationHelper.serialize_item(self.drop_not, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DROP-NOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_number_of
        if self.max_number_of is not None:
            serialized = SerializationHelper.serialize_item(self.max_number_of, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize p2_max
        if self.p2_max is not None:
            serialized = SerializationHelper.serialize_item(self.p2_max, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("P2-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize p2_timing
        if self.p2_timing is not None:
            serialized = SerializationHelper.serialize_item(self.p2_timing, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("P2-TIMING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_address_ref
        if self.tp_address_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tp_address_ref, "TpAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-ADDRESS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinTpNode":
        """Deserialize XML element to LinTpNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinTpNode object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinTpNode, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONNECTOR-REF":
                setattr(obj, "connector_ref", ARRef.deserialize(child))
            elif tag == "DROP-NOT":
                setattr(obj, "drop_not", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "MAX-NUMBER-OF":
                setattr(obj, "max_number_of", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "P2-MAX":
                setattr(obj, "p2_max", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "P2-TIMING":
                setattr(obj, "p2_timing", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TP-ADDRESS-REF":
                setattr(obj, "tp_address_ref", ARRef.deserialize(child))

        return obj



class LinTpNodeBuilder(IdentifiableBuilder):
    """Builder for LinTpNode with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LinTpNode = LinTpNode()


    def with_connector(self, value: Optional[any (Communication)]) -> "LinTpNodeBuilder":
        """Set connector attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.connector = value
        return self

    def with_drop_not(self, value: Optional[Boolean]) -> "LinTpNodeBuilder":
        """Set drop_not attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.drop_not = value
        return self

    def with_max_number_of(self, value: Optional[Integer]) -> "LinTpNodeBuilder":
        """Set max_number_of attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_number_of = value
        return self

    def with_p2_max(self, value: Optional[TimeValue]) -> "LinTpNodeBuilder":
        """Set p2_max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.p2_max = value
        return self

    def with_p2_timing(self, value: Optional[TimeValue]) -> "LinTpNodeBuilder":
        """Set p2_timing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.p2_timing = value
        return self

    def with_tp_address(self, value: Optional[TpAddress]) -> "LinTpNodeBuilder":
        """Set tp_address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tp_address = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "connector",
        "dropNot",
        "maxNumberOf",
        "p2Max",
        "p2Timing",
        "tpAddress",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> LinTpNode:
        """Build and return the LinTpNode instance with validation."""
        self._validate_instance()
        return self._obj