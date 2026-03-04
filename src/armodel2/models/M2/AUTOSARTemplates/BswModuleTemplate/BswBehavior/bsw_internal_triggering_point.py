"""BswInternalTriggeringPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwImplPolicyEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswInternalTriggeringPoint(Identifiable):
    """AUTOSAR BswInternalTriggeringPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-INTERNAL-TRIGGERING-POINT"


    sw_impl_policy: Optional[SwImplPolicyEnum]
    _DESERIALIZE_DISPATCH = {
        "SW-IMPL-POLICY": lambda obj, elem: setattr(obj, "sw_impl_policy", SwImplPolicyEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize BswInternalTriggeringPoint."""
        super().__init__()
        self.sw_impl_policy: Optional[SwImplPolicyEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize BswInternalTriggeringPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswInternalTriggeringPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_impl_policy
        if self.sw_impl_policy is not None:
            serialized = SerializationHelper.serialize_item(self.sw_impl_policy, "SwImplPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-IMPL-POLICY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswInternalTriggeringPoint":
        """Deserialize XML element to BswInternalTriggeringPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswInternalTriggeringPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswInternalTriggeringPoint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SW-IMPL-POLICY":
                setattr(obj, "sw_impl_policy", SwImplPolicyEnum.deserialize(child))

        return obj



class BswInternalTriggeringPointBuilder(IdentifiableBuilder):
    """Builder for BswInternalTriggeringPoint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswInternalTriggeringPoint = BswInternalTriggeringPoint()


    def with_sw_impl_policy(self, value: Optional[SwImplPolicyEnum]) -> "BswInternalTriggeringPointBuilder":
        """Set sw_impl_policy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_impl_policy = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "swImplPolicy",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswInternalTriggeringPoint:
        """Build and return the BswInternalTriggeringPoint instance with validation."""
        self._validate_instance()
        return self._obj