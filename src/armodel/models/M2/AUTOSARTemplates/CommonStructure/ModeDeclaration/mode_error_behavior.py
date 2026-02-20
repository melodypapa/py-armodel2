"""ModeErrorBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 44)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 637)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeErrorReactionPolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeErrorBehavior(ARObject):
    """AUTOSAR ModeErrorBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_mode_ref: Optional[ARRef]
    error_reaction: Optional[ModeErrorReactionPolicyEnum]
    def __init__(self) -> None:
        """Initialize ModeErrorBehavior."""
        super().__init__()
        self.default_mode_ref: Optional[ARRef] = None
        self.error_reaction: Optional[ModeErrorReactionPolicyEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeErrorBehavior to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize default_mode_ref
        if self.default_mode_ref is not None:
            serialized = ARObject._serialize_item(self.default_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize error_reaction
        if self.error_reaction is not None:
            serialized = ARObject._serialize_item(self.error_reaction, "ModeErrorReactionPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ERROR-REACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeErrorBehavior":
        """Deserialize XML element to ModeErrorBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeErrorBehavior object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse default_mode_ref
        child = ARObject._find_child_element(element, "DEFAULT-MODE-REF")
        if child is not None:
            default_mode_ref_value = ARRef.deserialize(child)
            obj.default_mode_ref = default_mode_ref_value

        # Parse error_reaction
        child = ARObject._find_child_element(element, "ERROR-REACTION")
        if child is not None:
            error_reaction_value = ModeErrorReactionPolicyEnum.deserialize(child)
            obj.error_reaction = error_reaction_value

        return obj



class ModeErrorBehaviorBuilder:
    """Builder for ModeErrorBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeErrorBehavior = ModeErrorBehavior()

    def build(self) -> ModeErrorBehavior:
        """Build and return ModeErrorBehavior object.

        Returns:
            ModeErrorBehavior instance
        """
        # TODO: Add validation
        return self._obj
