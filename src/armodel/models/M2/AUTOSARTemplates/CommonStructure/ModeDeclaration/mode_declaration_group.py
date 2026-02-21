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
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    initial_mode_ref: Optional[ARRef]
    mode_declarations: list[ModeDeclaration]
    mode_manager_error_behavior: Optional[ModeErrorBehavior]
    mode_transitions: list[ModeTransition]
    mode_user_error_behavior: Optional[ModeErrorBehavior]
    on_transition_value: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ModeDeclarationGroup."""
        super().__init__()
        self.initial_mode_ref: Optional[ARRef] = None
        self.mode_declarations: list[ModeDeclaration] = []
        self.mode_manager_error_behavior: Optional[ModeErrorBehavior] = None
        self.mode_transitions: list[ModeTransition] = []
        self.mode_user_error_behavior: Optional[ModeErrorBehavior] = None
        self.on_transition_value: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeDeclarationGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeDeclarationGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize initial_mode_ref
        if self.initial_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.initial_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_declarations (list to container "MODE-DECLARATIONS")
        if self.mode_declarations:
            wrapper = ET.Element("MODE-DECLARATIONS")
            for item in self.mode_declarations:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclaration")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_manager_error_behavior
        if self.mode_manager_error_behavior is not None:
            serialized = SerializationHelper.serialize_item(self.mode_manager_error_behavior, "ModeErrorBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-MANAGER-ERROR-BEHAVIOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_transitions (list to container "MODE-TRANSITIONS")
        if self.mode_transitions:
            wrapper = ET.Element("MODE-TRANSITIONS")
            for item in self.mode_transitions:
                serialized = SerializationHelper.serialize_item(item, "ModeTransition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_user_error_behavior
        if self.mode_user_error_behavior is not None:
            serialized = SerializationHelper.serialize_item(self.mode_user_error_behavior, "ModeErrorBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-USER-ERROR-BEHAVIOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize on_transition_value
        if self.on_transition_value is not None:
            serialized = SerializationHelper.serialize_item(self.on_transition_value, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ON-TRANSITION-VALUE")
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

        # Parse initial_mode_ref
        child = SerializationHelper.find_child_element(element, "INITIAL-MODE-REF")
        if child is not None:
            initial_mode_ref_value = ARRef.deserialize(child)
            obj.initial_mode_ref = initial_mode_ref_value

        # Parse mode_declarations (list from container "MODE-DECLARATIONS")
        obj.mode_declarations = []
        container = SerializationHelper.find_child_element(element, "MODE-DECLARATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_declarations.append(child_value)

        # Parse mode_manager_error_behavior
        child = SerializationHelper.find_child_element(element, "MODE-MANAGER-ERROR-BEHAVIOR")
        if child is not None:
            mode_manager_error_behavior_value = SerializationHelper.deserialize_by_tag(child, "ModeErrorBehavior")
            obj.mode_manager_error_behavior = mode_manager_error_behavior_value

        # Parse mode_transitions (list from container "MODE-TRANSITIONS")
        obj.mode_transitions = []
        container = SerializationHelper.find_child_element(element, "MODE-TRANSITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_transitions.append(child_value)

        # Parse mode_user_error_behavior
        child = SerializationHelper.find_child_element(element, "MODE-USER-ERROR-BEHAVIOR")
        if child is not None:
            mode_user_error_behavior_value = SerializationHelper.deserialize_by_tag(child, "ModeErrorBehavior")
            obj.mode_user_error_behavior = mode_user_error_behavior_value

        # Parse on_transition_value
        child = SerializationHelper.find_child_element(element, "ON-TRANSITION-VALUE")
        if child is not None:
            on_transition_value_value = child.text
            obj.on_transition_value = on_transition_value_value

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
