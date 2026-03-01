"""DiagnosticConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 60)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 632)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DiagnosticConnection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection_ident import (
    TpConnectionIdent,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticConnection(ARElement):
    """AUTOSAR DiagnosticConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-CONNECTION"


    functional_request_refs: list[ARRef]
    periodic_response_uudt_refs: list[ARRef]
    physical_request_ref: Optional[ARRef]
    response_ref: Optional[ARRef]
    response_on_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "FUNCTIONAL-REQUESTS": lambda obj, elem: obj.functional_request_refs.append(ARRef.deserialize(elem)),
        "PERIODIC-RESPONSE-UUDTS": lambda obj, elem: obj.periodic_response_uudt_refs.append(ARRef.deserialize(elem)),
        "PHYSICAL-REQUEST-REF": lambda obj, elem: setattr(obj, "physical_request_ref", ARRef.deserialize(elem)),
        "RESPONSE-REF": lambda obj, elem: setattr(obj, "response_ref", ARRef.deserialize(elem)),
        "RESPONSE-ON-REF": lambda obj, elem: setattr(obj, "response_on_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticConnection."""
        super().__init__()
        self.functional_request_refs: list[ARRef] = []
        self.periodic_response_uudt_refs: list[ARRef] = []
        self.physical_request_ref: Optional[ARRef] = None
        self.response_ref: Optional[ARRef] = None
        self.response_on_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize functional_request_refs (list to container "FUNCTIONAL-REQUEST-REFS")
        if self.functional_request_refs:
            wrapper = ET.Element("FUNCTIONAL-REQUEST-REFS")
            for item in self.functional_request_refs:
                serialized = SerializationHelper.serialize_item(item, "TpConnectionIdent")
                if serialized is not None:
                    child_elem = ET.Element("FUNCTIONAL-REQUEST-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize periodic_response_uudt_refs (list to container "PERIODIC-RESPONSE-UUDT-REFS")
        if self.periodic_response_uudt_refs:
            wrapper = ET.Element("PERIODIC-RESPONSE-UUDT-REFS")
            for item in self.periodic_response_uudt_refs:
                serialized = SerializationHelper.serialize_item(item, "PduTriggering")
                if serialized is not None:
                    child_elem = ET.Element("PERIODIC-RESPONSE-UUDT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize physical_request_ref
        if self.physical_request_ref is not None:
            serialized = SerializationHelper.serialize_item(self.physical_request_ref, "TpConnectionIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYSICAL-REQUEST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize response_ref
        if self.response_ref is not None:
            serialized = SerializationHelper.serialize_item(self.response_ref, "TpConnectionIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize response_on_ref
        if self.response_on_ref is not None:
            serialized = SerializationHelper.serialize_item(self.response_on_ref, "TpConnectionIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-ON-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticConnection":
        """Deserialize XML element to DiagnosticConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticConnection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "FUNCTIONAL-REQUESTS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.functional_request_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "TpConnectionIdent"))
            elif tag == "PERIODIC-RESPONSE-UUDTS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.periodic_response_uudt_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "PduTriggering"))
            elif tag == "PHYSICAL-REQUEST-REF":
                setattr(obj, "physical_request_ref", ARRef.deserialize(child))
            elif tag == "RESPONSE-REF":
                setattr(obj, "response_ref", ARRef.deserialize(child))
            elif tag == "RESPONSE-ON-REF":
                setattr(obj, "response_on_ref", ARRef.deserialize(child))

        return obj



class DiagnosticConnectionBuilder(ARElementBuilder):
    """Builder for DiagnosticConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticConnection = DiagnosticConnection()


    def with_functional_requests(self, items: list[TpConnectionIdent]) -> "DiagnosticConnectionBuilder":
        """Set functional_requests list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.functional_requests = list(items) if items else []
        return self

    def with_periodic_response_uudts(self, items: list[PduTriggering]) -> "DiagnosticConnectionBuilder":
        """Set periodic_response_uudts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.periodic_response_uudts = list(items) if items else []
        return self

    def with_physical_request(self, value: Optional[TpConnectionIdent]) -> "DiagnosticConnectionBuilder":
        """Set physical_request attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.physical_request = value
        return self

    def with_response(self, value: Optional[TpConnectionIdent]) -> "DiagnosticConnectionBuilder":
        """Set response attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.response = value
        return self

    def with_response_on(self, value: Optional[TpConnectionIdent]) -> "DiagnosticConnectionBuilder":
        """Set response_on attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.response_on = value
        return self


    def add_functional_request(self, item: TpConnectionIdent) -> "DiagnosticConnectionBuilder":
        """Add a single item to functional_requests list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.functional_requests.append(item)
        return self

    def clear_functional_requests(self) -> "DiagnosticConnectionBuilder":
        """Clear all items from functional_requests list.

        Returns:
            self for method chaining
        """
        self._obj.functional_requests = []
        return self

    def add_periodic_response_uudt(self, item: PduTriggering) -> "DiagnosticConnectionBuilder":
        """Add a single item to periodic_response_uudts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.periodic_response_uudts.append(item)
        return self

    def clear_periodic_response_uudts(self) -> "DiagnosticConnectionBuilder":
        """Clear all items from periodic_response_uudts list.

        Returns:
            self for method chaining
        """
        self._obj.periodic_response_uudts = []
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


    def build(self) -> DiagnosticConnection:
        """Build and return the DiagnosticConnection instance with validation."""
        self._validate_instance()
        pass
        return self._obj