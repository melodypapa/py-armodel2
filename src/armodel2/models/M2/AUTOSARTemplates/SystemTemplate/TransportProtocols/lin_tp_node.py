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
        "DROP-NOT": lambda obj, elem: setattr(obj, "drop_not", elem.text),
        "MAX-NUMBER-OF": lambda obj, elem: setattr(obj, "max_number_of", elem.text),
        "P2-MAX": lambda obj, elem: setattr(obj, "p2_max", elem.text),
        "P2-TIMING": lambda obj, elem: setattr(obj, "p2_timing", elem.text),
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

        # Parse connector_ref
        child = SerializationHelper.find_child_element(element, "CONNECTOR-REF")
        if child is not None:
            connector_ref_value = ARRef.deserialize(child)
            obj.connector_ref = connector_ref_value

        # Parse drop_not
        child = SerializationHelper.find_child_element(element, "DROP-NOT")
        if child is not None:
            drop_not_value = child.text
            obj.drop_not = drop_not_value

        # Parse max_number_of
        child = SerializationHelper.find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse p2_max
        child = SerializationHelper.find_child_element(element, "P2-MAX")
        if child is not None:
            p2_max_value = child.text
            obj.p2_max = p2_max_value

        # Parse p2_timing
        child = SerializationHelper.find_child_element(element, "P2-TIMING")
        if child is not None:
            p2_timing_value = child.text
            obj.p2_timing = p2_timing_value

        # Parse tp_address_ref
        child = SerializationHelper.find_child_element(element, "TP-ADDRESS-REF")
        if child is not None:
            tp_address_ref_value = ARRef.deserialize(child)
            obj.tp_address_ref = tp_address_ref_value

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


    def build(self) -> LinTpNode:
        """Build and return the LinTpNode instance with validation."""
        self._validate_instance()
        pass
        return self._obj