"""VariableAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 351)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 567)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2077)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 256)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import AbstractAccessPointBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
    VariableAccessScopeEnum,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
        AutosarVariableRef,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class VariableAccess(AbstractAccessPoint):
    """AUTOSAR VariableAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "VARIABLE-ACCESS"


    accessed_variable: Optional[AutosarVariableRef]
    scope: Optional[VariableAccessScopeEnum]
    _DESERIALIZE_DISPATCH = {
        "ACCESSED-VARIABLE": lambda obj, elem: setattr(obj, "accessed_variable", SerializationHelper.deserialize_by_tag(elem, "AutosarVariableRef")),
        "SCOPE": lambda obj, elem: setattr(obj, "scope", VariableAccessScopeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize VariableAccess."""
        super().__init__()
        self.accessed_variable: Optional[AutosarVariableRef] = None
        self.scope: Optional[VariableAccessScopeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize VariableAccess to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(VariableAccess, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize accessed_variable
        if self.accessed_variable is not None:
            serialized = SerializationHelper.serialize_item(self.accessed_variable, "AutosarVariableRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESSED-VARIABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize scope
        if self.scope is not None:
            serialized = SerializationHelper.serialize_item(self.scope, "VariableAccessScopeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SCOPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariableAccess":
        """Deserialize XML element to VariableAccess object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariableAccess object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(VariableAccess, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACCESSED-VARIABLE":
                setattr(obj, "accessed_variable", SerializationHelper.deserialize_by_tag(child, "AutosarVariableRef"))
            elif tag == "SCOPE":
                setattr(obj, "scope", VariableAccessScopeEnum.deserialize(child))

        return obj



class VariableAccessBuilder(AbstractAccessPointBuilder):
    """Builder for VariableAccess with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: VariableAccess = VariableAccess()


    def with_accessed_variable(self, value: Optional[AutosarVariableRef]) -> "VariableAccessBuilder":
        """Set accessed_variable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'accessed_variable' is required and cannot be None")
        self._obj.accessed_variable = value
        return self

    def with_scope(self, value: Optional[VariableAccessScopeEnum]) -> "VariableAccessBuilder":
        """Set scope attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'scope' is required and cannot be None")
        self._obj.scope = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "accessedVariable",
        "scope",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> VariableAccess:
        """Build and return the VariableAccess instance with validation."""
        self._validate_instance()
        return self._obj