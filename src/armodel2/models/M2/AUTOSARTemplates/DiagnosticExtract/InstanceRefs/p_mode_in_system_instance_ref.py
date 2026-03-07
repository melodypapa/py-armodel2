"""PModeInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PModeInSystemInstanceRef(ARObject):
    """AUTOSAR PModeInSystemInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "P-MODE-IN-SYSTEM-INSTANCE-REF"


    base_ref: Optional[ARRef]
    context_ref: Optional[ARRef]
    context_mode_group_ref: Optional[ARRef]
    context_p_port_prototype_ref: Optional[ARRef]
    target_mode_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BASE-REF": lambda obj, elem: setattr(obj, "base_ref", ARRef.deserialize(elem)),
        "CONTEXT-REF": lambda obj, elem: setattr(obj, "context_ref", ARRef.deserialize(elem)),
        "CONTEXT-MODE-GROUP-REF": lambda obj, elem: setattr(obj, "context_mode_group_ref", ARRef.deserialize(elem)),
        "CONTEXT-P-PORT-PROTOTYPE-REF": ("_POLYMORPHIC", "context_p_port_prototype_ref", ["PPortPrototype", "PRPortPrototype"]),
        "TARGET-MODE-REF": lambda obj, elem: setattr(obj, "target_mode_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize PModeInSystemInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_ref: Optional[ARRef] = None
        self.context_mode_group_ref: Optional[ARRef] = None
        self.context_p_port_prototype_ref: Optional[ARRef] = None
        self.target_mode_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize PModeInSystemInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PModeInSystemInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_ref, "System")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_ref
        if self.context_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_ref, "RootSwCompositionPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_mode_group_ref
        if self.context_mode_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_mode_group_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-MODE-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_p_port_prototype_ref
        if self.context_p_port_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_p_port_prototype_ref, "AbstractProvidedPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-P-PORT-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_mode_ref
        if self.target_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PModeInSystemInstanceRef":
        """Deserialize XML element to PModeInSystemInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PModeInSystemInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PModeInSystemInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BASE-REF":
                setattr(obj, "base_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-REF":
                setattr(obj, "context_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-MODE-GROUP-REF":
                setattr(obj, "context_mode_group_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-P-PORT-PROTOTYPE-REF":
                setattr(obj, "context_p_port_prototype_ref", ARRef.deserialize(child))
            elif tag == "TARGET-MODE-REF":
                setattr(obj, "target_mode_ref", ARRef.deserialize(child))

        return obj



class PModeInSystemInstanceRefBuilder(BuilderBase):
    """Builder for PModeInSystemInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PModeInSystemInstanceRef = PModeInSystemInstanceRef()


    def with_base(self, value: Optional[System]) -> "PModeInSystemInstanceRefBuilder":
        """Set base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'base' is required and cannot be None")
        self._obj.base = value
        return self

    def with_context(self, value: Optional[RootSwCompositionPrototype]) -> "PModeInSystemInstanceRefBuilder":
        """Set context attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'context' is required and cannot be None")
        self._obj.context = value
        return self

    def with_context_mode_group(self, value: Optional[ModeDeclarationGroup]) -> "PModeInSystemInstanceRefBuilder":
        """Set context_mode_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'context_mode_group' is required and cannot be None")
        self._obj.context_mode_group = value
        return self

    def with_context_p_port_prototype(self, value: Optional[AbstractProvidedPortPrototype]) -> "PModeInSystemInstanceRefBuilder":
        """Set context_p_port_prototype attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'context_p_port_prototype' is required and cannot be None")
        self._obj.context_p_port_prototype = value
        return self

    def with_target_mode(self, value: Optional[ModeDeclaration]) -> "PModeInSystemInstanceRefBuilder":
        """Set target_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'target_mode' is required and cannot be None")
        self._obj.target_mode = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "base",
        "context",
        "contextModeGroup",
        "contextPPortPrototype",
        "targetMode",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PModeInSystemInstanceRef:
        """Build and return the PModeInSystemInstanceRef instance with validation."""
        self._validate_instance()
        return self._obj