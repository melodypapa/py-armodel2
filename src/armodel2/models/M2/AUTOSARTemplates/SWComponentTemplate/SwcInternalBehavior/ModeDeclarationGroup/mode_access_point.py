"""ModeAccessPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 323)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 634)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ModeDeclarationGroup.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import polymorphic

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.mode_access_point_ident import (
    ModeAccessPointIdent,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.mode_group_in_atomic_swc_instance_ref import (
        ModeGroupInAtomicSwcInstanceRef,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ModeAccessPoint(ARObject):
    """AUTOSAR ModeAccessPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-ACCESS-POINT"


    ident: Optional[ModeAccessPointIdent]
    _mode_group_iref: Optional[ModeGroupInAtomicSwcInstanceRef]
    _DESERIALIZE_DISPATCH = {
        "IDENT": lambda obj, elem: setattr(obj, "ident", SerializationHelper.deserialize_by_tag(elem, "ModeAccessPointIdent")),
        "MODE-GROUP-IREF": ("_POLYMORPHIC", "_mode_group_iref", ["PModeGroupInAtomicSwcInstanceRef", "RModeGroupInAtomicSWCInstanceRef"]),
    }


    def __init__(self) -> None:
        """Initialize ModeAccessPoint."""
        super().__init__()
        self.ident: Optional[ModeAccessPointIdent] = None
        self._mode_group_iref: Optional[ModeGroupInAtomicSwcInstanceRef] = None
    @property
    @polymorphic({"MODE-GROUP-IREF": "ModeGroupInAtomicSwcInstanceRef"})
    def mode_group_iref(self) -> Optional[ModeGroupInAtomicSwcInstanceRef]:
        """Get mode_group_iref with polymorphic wrapper handling."""
        return self._mode_group_iref

    @mode_group_iref.setter
    def mode_group_iref(self, value: Optional[ModeGroupInAtomicSwcInstanceRef]) -> None:
        """Set mode_group_iref with polymorphic wrapper handling."""
        self._mode_group_iref = value


    def serialize(self) -> ET.Element:
        """Serialize ModeAccessPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeAccessPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ident
        if self.ident is not None:
            serialized = SerializationHelper.serialize_item(self.ident, "ModeAccessPointIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_group_iref (polymorphic wrapper "MODE-GROUP-IREF")
        if self.mode_group_iref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_group_iref, "ModeGroupInAtomicSwcInstanceRef")
            if serialized is not None:
                # For polymorphic types, wrap the serialized element (preserving concrete type)
                wrapped = ET.Element("MODE-GROUP-IREF")
                wrapped.append(serialized)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeAccessPoint":
        """Deserialize XML element to ModeAccessPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeAccessPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeAccessPoint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IDENT":
                setattr(obj, "ident", SerializationHelper.deserialize_by_tag(child, "ModeAccessPointIdent"))
            elif tag == "MODE-GROUP-IREF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF":
                        setattr(obj, "_mode_group_iref", SerializationHelper.deserialize_by_tag(child[0], "PModeGroupInAtomicSwcInstanceRef"))
                    elif concrete_tag == "R-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF":
                        setattr(obj, "_mode_group_iref", SerializationHelper.deserialize_by_tag(child[0], "RModeGroupInAtomicSWCInstanceRef"))

        return obj



class ModeAccessPointBuilder(BuilderBase):
    """Builder for ModeAccessPoint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeAccessPoint = ModeAccessPoint()


    def with_ident(self, value: Optional[ModeAccessPointIdent]) -> "ModeAccessPointBuilder":
        """Set ident attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'ident' is required and cannot be None")
        self._obj.ident = value
        return self

    def with_mode_group(self, value: Optional[ModeGroupInAtomicSwcInstanceRef]) -> "ModeAccessPointBuilder":
        """Set mode_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'mode_group' is required and cannot be None")
        self._obj.mode_group = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ident",
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


    def build(self) -> ModeAccessPoint:
        """Build and return the ModeAccessPoint instance with validation."""
        self._validate_instance()
        return self._obj