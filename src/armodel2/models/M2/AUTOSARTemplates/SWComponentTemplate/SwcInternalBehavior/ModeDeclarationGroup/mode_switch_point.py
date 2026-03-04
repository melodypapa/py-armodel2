"""ModeSwitchPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 323)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 633)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ModeDeclarationGroup.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import AbstractAccessPointBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.p_mode_group_in_atomic_swc_instance_ref import (
        PModeGroupInAtomicSwcInstanceRef,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ModeSwitchPoint(AbstractAccessPoint):
    """AUTOSAR ModeSwitchPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-SWITCH-POINT"


    mode_group_iref: Optional[PModeGroupInAtomicSwcInstanceRef]
    _DESERIALIZE_DISPATCH = {
        "MODE-GROUP-IREF": lambda obj, elem: setattr(obj, "mode_group_iref", SerializationHelper.deserialize_by_tag(elem, "PModeGroupInAtomicSwcInstanceRef")),
    }


    def __init__(self) -> None:
        """Initialize ModeSwitchPoint."""
        super().__init__()
        self.mode_group_iref: Optional[PModeGroupInAtomicSwcInstanceRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeSwitchPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeSwitchPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mode_group_iref (instance reference with wrapper "MODE-GROUP-IREF")
        if self.mode_group_iref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_group_iref, "PModeGroupInAtomicSwcInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("MODE-GROUP-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchPoint":
        """Deserialize XML element to ModeSwitchPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeSwitchPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeSwitchPoint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MODE-GROUP-IREF":
                setattr(obj, "mode_group_iref", SerializationHelper.deserialize_by_tag(child, "PModeGroupInAtomicSwcInstanceRef"))

        return obj



class ModeSwitchPointBuilder(AbstractAccessPointBuilder):
    """Builder for ModeSwitchPoint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeSwitchPoint = ModeSwitchPoint()


    def with_mode_group(self, value: Optional[PModeGroupInAtomicSwcInstanceRef]) -> "ModeSwitchPointBuilder":
        """Set mode_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mode_group = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "modeGroup",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ModeSwitchPoint:
        """Build and return the ModeSwitchPoint instance with validation."""
        self._validate_instance()
        return self._obj