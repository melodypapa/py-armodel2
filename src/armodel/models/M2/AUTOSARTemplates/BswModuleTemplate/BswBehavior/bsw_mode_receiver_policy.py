"""BswModeReceiverPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class BswModeReceiverPolicy(ARObject):
    """AUTOSAR BswModeReceiverPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    enhanced_mode: Optional[Boolean]
    required_mode_ref: Optional[ARRef]
    supports: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize BswModeReceiverPolicy."""
        super().__init__()
        self.enhanced_mode: Optional[Boolean] = None
        self.required_mode_ref: Optional[ARRef] = None
        self.supports: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize BswModeReceiverPolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize enhanced_mode
        if self.enhanced_mode is not None:
            serialized = ARObject._serialize_item(self.enhanced_mode, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENHANCED-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize required_mode_ref
        if self.required_mode_ref is not None:
            serialized = ARObject._serialize_item(self.required_mode_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRED-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize supports
        if self.supports is not None:
            serialized = ARObject._serialize_item(self.supports, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModeReceiverPolicy":
        """Deserialize XML element to BswModeReceiverPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModeReceiverPolicy object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse enhanced_mode
        child = ARObject._find_child_element(element, "ENHANCED-MODE")
        if child is not None:
            enhanced_mode_value = child.text
            obj.enhanced_mode = enhanced_mode_value

        # Parse required_mode_ref
        child = ARObject._find_child_element(element, "REQUIRED-MODE-REF")
        if child is not None:
            required_mode_ref_value = ARRef.deserialize(child)
            obj.required_mode_ref = required_mode_ref_value

        # Parse supports
        child = ARObject._find_child_element(element, "SUPPORTS")
        if child is not None:
            supports_value = child.text
            obj.supports = supports_value

        return obj



class BswModeReceiverPolicyBuilder:
    """Builder for BswModeReceiverPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeReceiverPolicy = BswModeReceiverPolicy()

    def build(self) -> BswModeReceiverPolicy:
        """Build and return BswModeReceiverPolicy object.

        Returns:
            BswModeReceiverPolicy instance
        """
        # TODO: Add validation
        return self._obj
