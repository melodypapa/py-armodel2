"""BswModuleDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 47)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.bsw_module_description import (
        BswModuleDescription,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class BswModuleDependency(Identifiable):
    """AUTOSAR BswModuleDependency."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-MODULE-DEPENDENCY"


    target_module_id: Optional[PositiveInteger]
    target_module_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "TARGET-MODULE-ID": lambda obj, elem: setattr(obj, "target_module_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TARGET-MODULE-REF": lambda obj, elem: setattr(obj, "target_module_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize BswModuleDependency."""
        super().__init__()
        self.target_module_id: Optional[PositiveInteger] = None
        self.target_module_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BswModuleDependency to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModuleDependency, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize target_module_id
        if self.target_module_id is not None:
            serialized = SerializationHelper.serialize_item(self.target_module_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODULE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_module_ref
        if self.target_module_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_module_ref, "BswModuleDescription")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODULE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleDependency":
        """Deserialize XML element to BswModuleDependency object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModuleDependency object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModuleDependency, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TARGET-MODULE-ID":
                setattr(obj, "target_module_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TARGET-MODULE-REF":
                setattr(obj, "target_module_ref", ARRef.deserialize(child))

        return obj



class BswModuleDependencyBuilder(IdentifiableBuilder):
    """Builder for BswModuleDependency with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswModuleDependency = BswModuleDependency()


    def with_target_module_id(self, value: Optional[PositiveInteger]) -> "BswModuleDependencyBuilder":
        """Set target_module_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'target_module_id' is required and cannot be None")
        self._obj.target_module_id = value
        return self

    def with_target_module(self, value: Optional[BswModuleDescription]) -> "BswModuleDependencyBuilder":
        """Set target_module attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'target_module' is required and cannot be None")
        self._obj.target_module = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "targetModule",
        "targetModuleId",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswModuleDependency:
        """Build and return the BswModuleDependency instance with validation."""
        self._validate_instance()
        return self._obj