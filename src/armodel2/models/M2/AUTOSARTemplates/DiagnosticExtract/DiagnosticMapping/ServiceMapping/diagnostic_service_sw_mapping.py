"""DiagnosticServiceSwMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 238)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import DiagnosticSwMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticServiceSwMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticServiceSwMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accessed_data_ref: Optional[ARRef]
    diagnostic_data_ref: Optional[ARRef]
    diagnostic_ref: Optional[ARRef]
    mapped_bsw_ref: Optional[Any]
    mapped_flat_swc_ref: Optional[Any]
    mapped_swc: Optional[Any]
    parameter: Optional[DiagnosticParameter]
    service_instance_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticServiceSwMapping."""
        super().__init__()
        self.accessed_data_ref: Optional[ARRef] = None
        self.diagnostic_data_ref: Optional[ARRef] = None
        self.diagnostic_ref: Optional[ARRef] = None
        self.mapped_bsw_ref: Optional[Any] = None
        self.mapped_flat_swc_ref: Optional[Any] = None
        self.mapped_swc: Optional[Any] = None
        self.parameter: Optional[DiagnosticParameter] = None
        self.service_instance_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticServiceSwMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticServiceSwMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize accessed_data_ref
        if self.accessed_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.accessed_data_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESSED-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic_data_ref
        if self.diagnostic_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic_data_ref, "DiagnosticDataElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic_ref
        if self.diagnostic_ref is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic_ref, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapped_bsw_ref
        if self.mapped_bsw_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mapped_bsw_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPED-BSW-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapped_flat_swc_ref
        if self.mapped_flat_swc_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mapped_flat_swc_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPED-FLAT-SWC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapped_swc
        if self.mapped_swc is not None:
            serialized = SerializationHelper.serialize_item(self.mapped_swc, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPED-SWC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize parameter
        if self.parameter is not None:
            serialized = SerializationHelper.serialize_item(self.parameter, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PARAMETER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_instance_ref
        if self.service_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.service_instance_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceSwMapping":
        """Deserialize XML element to DiagnosticServiceSwMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticServiceSwMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticServiceSwMapping, cls).deserialize(element)

        # Parse accessed_data_ref
        child = SerializationHelper.find_child_element(element, "ACCESSED-DATA-REF")
        if child is not None:
            accessed_data_ref_value = ARRef.deserialize(child)
            obj.accessed_data_ref = accessed_data_ref_value

        # Parse diagnostic_data_ref
        child = SerializationHelper.find_child_element(element, "DIAGNOSTIC-DATA-REF")
        if child is not None:
            diagnostic_data_ref_value = ARRef.deserialize(child)
            obj.diagnostic_data_ref = diagnostic_data_ref_value

        # Parse diagnostic_ref
        child = SerializationHelper.find_child_element(element, "DIAGNOSTIC-REF")
        if child is not None:
            diagnostic_ref_value = ARRef.deserialize(child)
            obj.diagnostic_ref = diagnostic_ref_value

        # Parse mapped_bsw_ref
        child = SerializationHelper.find_child_element(element, "MAPPED-BSW-REF")
        if child is not None:
            mapped_bsw_ref_value = ARRef.deserialize(child)
            obj.mapped_bsw_ref = mapped_bsw_ref_value

        # Parse mapped_flat_swc_ref
        child = SerializationHelper.find_child_element(element, "MAPPED-FLAT-SWC-REF")
        if child is not None:
            mapped_flat_swc_ref_value = ARRef.deserialize(child)
            obj.mapped_flat_swc_ref = mapped_flat_swc_ref_value

        # Parse mapped_swc
        child = SerializationHelper.find_child_element(element, "MAPPED-SWC")
        if child is not None:
            mapped_swc_value = child.text
            obj.mapped_swc = mapped_swc_value

        # Parse parameter
        child = SerializationHelper.find_child_element(element, "PARAMETER")
        if child is not None:
            parameter_value = SerializationHelper.deserialize_by_tag(child, "DiagnosticParameter")
            obj.parameter = parameter_value

        # Parse service_instance_ref
        child = SerializationHelper.find_child_element(element, "SERVICE-INSTANCE-REF")
        if child is not None:
            service_instance_ref_value = ARRef.deserialize(child)
            obj.service_instance_ref = service_instance_ref_value

        return obj



class DiagnosticServiceSwMappingBuilder(DiagnosticSwMappingBuilder):
    """Builder for DiagnosticServiceSwMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticServiceSwMapping = DiagnosticServiceSwMapping()


    def with_accessed_data(self, value: Optional[DataPrototype]) -> "DiagnosticServiceSwMappingBuilder":
        """Set accessed_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.accessed_data = value
        return self

    def with_diagnostic_data(self, value: Optional[DiagnosticDataElement]) -> "DiagnosticServiceSwMappingBuilder":
        """Set diagnostic_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diagnostic_data = value
        return self

    def with_diagnostic(self, value: Optional[DiagnosticParameter]) -> "DiagnosticServiceSwMappingBuilder":
        """Set diagnostic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diagnostic = value
        return self

    def with_mapped_bsw(self, value: Optional[any (BswService)]) -> "DiagnosticServiceSwMappingBuilder":
        """Set mapped_bsw attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mapped_bsw = value
        return self

    def with_mapped_flat_swc(self, value: Optional[any (SwcService)]) -> "DiagnosticServiceSwMappingBuilder":
        """Set mapped_flat_swc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mapped_flat_swc = value
        return self

    def with_mapped_swc(self, value: Optional[any (SwcService)]) -> "DiagnosticServiceSwMappingBuilder":
        """Set mapped_swc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mapped_swc = value
        return self

    def with_parameter(self, value: Optional[DiagnosticParameter]) -> "DiagnosticServiceSwMappingBuilder":
        """Set parameter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.parameter = value
        return self

    def with_service_instance(self, value: Optional[any (DiagnosticService)]) -> "DiagnosticServiceSwMappingBuilder":
        """Set service_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_instance = value
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


    def build(self) -> DiagnosticServiceSwMapping:
        """Build and return the DiagnosticServiceSwMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj