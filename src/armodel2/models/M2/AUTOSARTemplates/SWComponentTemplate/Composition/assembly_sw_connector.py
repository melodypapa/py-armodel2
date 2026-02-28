"""AssemblySwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 289)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 80)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2000)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 423)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import instance_ref
from armodel2.serialization.decorators import ref_conditional

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import SwConnectorBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.p_port_in_composition_instance_ref import (
    PPortInCompositionInstanceRef,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.r_port_in_composition_instance_ref import (
    RPortInCompositionInstanceRef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AssemblySwConnector(SwConnector):
    """AUTOSAR AssemblySwConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ASSEMBLY-SW-CONNECTOR"


    _provider_iref: Optional[PPortInCompositionInstanceRef]
    _requester_iref: Optional[RPortInCompositionInstanceRef]
    _DESERIALIZE_DISPATCH = {
        "PROVIDER": lambda obj, elem: setattr(obj, "_provider_iref", ARRef.deserialize(elem)),
        "REQUESTER": lambda obj, elem: setattr(obj, "_requester_iref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize AssemblySwConnector."""
        super().__init__()
        self._provider_iref: Optional[PPortInCompositionInstanceRef] = None
        self._requester_iref: Optional[RPortInCompositionInstanceRef] = None
    @property
    @instance_ref(flatten=True)
    def provider_iref(self) -> Optional[PPortInCompositionInstanceRef]:
        """Get provider_iref instance reference."""
        return self._provider_iref

    @provider_iref.setter
    def provider_iref(self, value: Optional[PPortInCompositionInstanceRef]) -> None:
        """Set provider_iref instance reference."""
        self._provider_iref = value

    @property
    @instance_ref(flatten=True)
    def requester_iref(self) -> Optional[RPortInCompositionInstanceRef]:
        """Get requester_iref instance reference."""
        return self._requester_iref

    @requester_iref.setter
    def requester_iref(self, value: Optional[RPortInCompositionInstanceRef]) -> None:
        """Set requester_iref instance reference."""
        self._requester_iref = value


    def serialize(self) -> ET.Element:
        """Serialize AssemblySwConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AssemblySwConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provider_iref (instance reference with wrapper "PROVIDER-IREF")
        if self.provider_iref is not None:
            serialized = SerializationHelper.serialize_item(self.provider_iref, "PPortInCompositionInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("PROVIDER-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        # Serialize requester_iref (instance reference with wrapper "REQUESTER-IREF")
        if self.requester_iref is not None:
            serialized = SerializationHelper.serialize_item(self.requester_iref, "RPortInCompositionInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("REQUESTER-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AssemblySwConnector":
        """Deserialize XML element to AssemblySwConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AssemblySwConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AssemblySwConnector, cls).deserialize(element)

        # Parse provider_iref (instance reference from wrapper "PROVIDER-IREF")
        wrapper = SerializationHelper.find_child_element(element, "PROVIDER-IREF")
        if wrapper is not None:
            # Deserialize wrapper element directly as the type (flattened structure)
            provider_iref_value = SerializationHelper.deserialize_by_tag(wrapper, "PPortInCompositionInstanceRef")
            obj.provider_iref = provider_iref_value

        # Parse requester_iref (instance reference from wrapper "REQUESTER-IREF")
        wrapper = SerializationHelper.find_child_element(element, "REQUESTER-IREF")
        if wrapper is not None:
            # Deserialize wrapper element directly as the type (flattened structure)
            requester_iref_value = SerializationHelper.deserialize_by_tag(wrapper, "RPortInCompositionInstanceRef")
            obj.requester_iref = requester_iref_value

        return obj



class AssemblySwConnectorBuilder(SwConnectorBuilder):
    """Builder for AssemblySwConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AssemblySwConnector = AssemblySwConnector()


    def with_provider(self, value: Optional[PPortInCompositionInstanceRef]) -> "AssemblySwConnectorBuilder":
        """Set provider attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.provider = value
        return self

    def with_requester(self, value: Optional[RPortInCompositionInstanceRef]) -> "AssemblySwConnectorBuilder":
        """Set requester attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.requester = value
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


    def build(self) -> AssemblySwConnector:
        """Build and return the AssemblySwConnector instance with validation."""
        self._validate_instance()
        pass
        return self._obj