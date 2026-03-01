"""DiagnosticTroubleCodeJ1939 AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 221)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import DiagnosticTroubleCodeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_spn import (
    DiagnosticJ1939Spn,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticTroubleCodeJ1939(DiagnosticTroubleCode):
    """AUTOSAR DiagnosticTroubleCodeJ1939."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-TROUBLE-CODE-J1939"


    dtc_props_props_ref: Optional[ARRef]
    fmi: Optional[PositiveInteger]
    kind: Optional[DiagnosticTroubleCode]
    node_ref: Optional[ARRef]
    spn_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DTC-PROPS-PROPS-REF": ("_POLYMORPHIC", "dtc_props_props_ref", ["DiagnosticTroubleCodeJ1939", "DiagnosticTroubleCodeObd", "DiagnosticTroubleCodeUds"]),
        "FMI": lambda obj, elem: setattr(obj, "fmi", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "KIND": ("_POLYMORPHIC", "kind", ["DiagnosticTroubleCodeJ1939", "DiagnosticTroubleCodeObd", "DiagnosticTroubleCodeUds"]),
        "NODE-REF": lambda obj, elem: setattr(obj, "node_ref", ARRef.deserialize(elem)),
        "SPN-REF": lambda obj, elem: setattr(obj, "spn_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeJ1939."""
        super().__init__()
        self.dtc_props_props_ref: Optional[ARRef] = None
        self.fmi: Optional[PositiveInteger] = None
        self.kind: Optional[DiagnosticTroubleCode] = None
        self.node_ref: Optional[ARRef] = None
        self.spn_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTroubleCodeJ1939 to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTroubleCodeJ1939, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dtc_props_props_ref
        if self.dtc_props_props_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dtc_props_props_ref, "DiagnosticTroubleCode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DTC-PROPS-PROPS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize fmi
        if self.fmi is not None:
            serialized = SerializationHelper.serialize_item(self.fmi, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FMI")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize kind
        if self.kind is not None:
            serialized = SerializationHelper.serialize_item(self.kind, "DiagnosticTroubleCode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize node_ref
        if self.node_ref is not None:
            serialized = SerializationHelper.serialize_item(self.node_ref, "DiagnosticJ1939Node")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize spn_ref
        if self.spn_ref is not None:
            serialized = SerializationHelper.serialize_item(self.spn_ref, "DiagnosticJ1939Spn")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SPN-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeJ1939":
        """Deserialize XML element to DiagnosticTroubleCodeJ1939 object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTroubleCodeJ1939 object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticTroubleCodeJ1939, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DTC-PROPS-PROPS-REF":
                setattr(obj, "dtc_props_props_ref", ARRef.deserialize(child))
            elif tag == "FMI":
                setattr(obj, "fmi", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "KIND":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "DIAGNOSTIC-TROUBLE-CODE-J1939":
                        setattr(obj, "kind", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticTroubleCodeJ1939"))
                    elif concrete_tag == "DIAGNOSTIC-TROUBLE-CODE-OBD":
                        setattr(obj, "kind", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticTroubleCodeObd"))
                    elif concrete_tag == "DIAGNOSTIC-TROUBLE-CODE-UDS":
                        setattr(obj, "kind", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticTroubleCodeUds"))
            elif tag == "NODE-REF":
                setattr(obj, "node_ref", ARRef.deserialize(child))
            elif tag == "SPN-REF":
                setattr(obj, "spn_ref", ARRef.deserialize(child))

        return obj



class DiagnosticTroubleCodeJ1939Builder(DiagnosticTroubleCodeBuilder):
    """Builder for DiagnosticTroubleCodeJ1939 with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticTroubleCodeJ1939 = DiagnosticTroubleCodeJ1939()


    def with_dtc_props_props(self, value: Optional[DiagnosticTroubleCode]) -> "DiagnosticTroubleCodeJ1939Builder":
        """Set dtc_props_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dtc_props_props = value
        return self

    def with_fmi(self, value: Optional[PositiveInteger]) -> "DiagnosticTroubleCodeJ1939Builder":
        """Set fmi attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.fmi = value
        return self

    def with_kind(self, value: Optional[DiagnosticTroubleCode]) -> "DiagnosticTroubleCodeJ1939Builder":
        """Set kind attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.kind = value
        return self

    def with_node(self, value: Optional[DiagnosticJ1939Node]) -> "DiagnosticTroubleCodeJ1939Builder":
        """Set node attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.node = value
        return self

    def with_spn(self, value: Optional[DiagnosticJ1939Spn]) -> "DiagnosticTroubleCodeJ1939Builder":
        """Set spn attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.spn = value
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


    def build(self) -> DiagnosticTroubleCodeJ1939:
        """Build and return the DiagnosticTroubleCodeJ1939 instance with validation."""
        self._validate_instance()
        pass
        return self._obj