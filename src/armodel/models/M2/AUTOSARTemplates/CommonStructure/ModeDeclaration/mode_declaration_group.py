"""ModeDeclarationGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 42)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 322)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 628)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2038)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 197)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_error_behavior import (
    ModeErrorBehavior,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_transition import (
    ModeTransition,
)


class ModeDeclarationGroup(ARElement):
    """AUTOSAR ModeDeclarationGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    initial_mode: Optional[ModeDeclaration]
    modes: list[ModeDeclaration]
    mode_manager: Optional[ModeErrorBehavior]
    mode_transition_mode_declaration_groups: list[ModeTransition]
    mode_user_error: Optional[ModeErrorBehavior]
    on_transition: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ModeDeclarationGroup."""
        super().__init__()
        self.initial_mode: Optional[ModeDeclaration] = None
        self.modes: list[ModeDeclaration] = []
        self.mode_manager: Optional[ModeErrorBehavior] = None
        self.mode_transition_mode_declaration_groups: list[ModeTransition] = []
        self.mode_user_error: Optional[ModeErrorBehavior] = None
        self.on_transition: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize ModeDeclarationGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeDeclarationGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize initial_mode
        if self.initial_mode is not None:
            serialized = ARObject._serialize_item(self.initial_mode, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize modes (list to container "MODES")
        if self.modes:
            wrapper = ET.Element("MODES")
            for item in self.modes:
                serialized = ARObject._serialize_item(item, "ModeDeclaration")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_manager
        if self.mode_manager is not None:
            serialized = ARObject._serialize_item(self.mode_manager, "ModeErrorBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-MANAGER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_transition_mode_declaration_groups (list to container "MODE-TRANSITION-MODE-DECLARATION-GROUPS")
        if self.mode_transition_mode_declaration_groups:
            wrapper = ET.Element("MODE-TRANSITION-MODE-DECLARATION-GROUPS")
            for item in self.mode_transition_mode_declaration_groups:
                serialized = ARObject._serialize_item(item, "ModeTransition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_user_error
        if self.mode_user_error is not None:
            serialized = ARObject._serialize_item(self.mode_user_error, "ModeErrorBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-USER-ERROR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize on_transition
        if self.on_transition is not None:
            serialized = ARObject._serialize_item(self.on_transition, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ON-TRANSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationGroup":
        """Deserialize XML element to ModeDeclarationGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeDeclarationGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeDeclarationGroup, cls).deserialize(element)

        # Parse initial_mode
        child = ARObject._find_child_element(element, "INITIAL-MODE")
        if child is not None:
            initial_mode_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.initial_mode = initial_mode_value

        # Parse modes (list from container "MODES")
        obj.modes = []
        container = ARObject._find_child_element(element, "MODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.modes.append(child_value)

        # Parse mode_manager
        child = ARObject._find_child_element(element, "MODE-MANAGER")
        if child is not None:
            mode_manager_value = ARObject._deserialize_by_tag(child, "ModeErrorBehavior")
            obj.mode_manager = mode_manager_value

        # Parse mode_transition_mode_declaration_groups (list from container "MODE-TRANSITION-MODE-DECLARATION-GROUPS")
        obj.mode_transition_mode_declaration_groups = []
        container = ARObject._find_child_element(element, "MODE-TRANSITION-MODE-DECLARATION-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_transition_mode_declaration_groups.append(child_value)

        # Parse mode_user_error
        child = ARObject._find_child_element(element, "MODE-USER-ERROR")
        if child is not None:
            mode_user_error_value = ARObject._deserialize_by_tag(child, "ModeErrorBehavior")
            obj.mode_user_error = mode_user_error_value

        # Parse on_transition
        child = ARObject._find_child_element(element, "ON-TRANSITION")
        if child is not None:
            on_transition_value = child.text
            obj.on_transition = on_transition_value

        return obj



class ModeDeclarationGroupBuilder:
    """Builder for ModeDeclarationGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclarationGroup = ModeDeclarationGroup()

    def build(self) -> ModeDeclarationGroup:
        """Build and return ModeDeclarationGroup object.

        Returns:
            ModeDeclarationGroup instance
        """
        # TODO: Add validation
        return self._obj
