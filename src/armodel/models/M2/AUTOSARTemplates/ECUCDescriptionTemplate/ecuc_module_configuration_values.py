"""EcucModuleConfigurationValues AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 313)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 110)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 441)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RevisionLabelString,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
    EcucModuleDef,
)


class EcucModuleConfigurationValues(ARElement):
    """AUTOSAR EcucModuleConfigurationValues."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    containers: list[EcucContainerValue]
    definition: Optional[EcucModuleDef]
    ecuc_def_edition: Optional[RevisionLabelString]
    implementation: Optional[Any]
    module: Optional[BswImplementation]
    post_build_variant: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucModuleConfigurationValues."""
        super().__init__()
        self.containers: list[EcucContainerValue] = []
        self.definition: Optional[EcucModuleDef] = None
        self.ecuc_def_edition: Optional[RevisionLabelString] = None
        self.implementation: Optional[Any] = None
        self.module: Optional[BswImplementation] = None
        self.post_build_variant: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucModuleConfigurationValues to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucModuleConfigurationValues, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize containers (list to container "CONTAINERS")
        if self.containers:
            wrapper = ET.Element("CONTAINERS")
            for item in self.containers:
                serialized = ARObject._serialize_item(item, "EcucContainerValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize definition
        if self.definition is not None:
            serialized = ARObject._serialize_item(self.definition, "EcucModuleDef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFINITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecuc_def_edition
        if self.ecuc_def_edition is not None:
            serialized = ARObject._serialize_item(self.ecuc_def_edition, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECUC-DEF-EDITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize implementation
        if self.implementation is not None:
            serialized = ARObject._serialize_item(self.implementation, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPLEMENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize module
        if self.module is not None:
            serialized = ARObject._serialize_item(self.module, "BswImplementation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize post_build_variant
        if self.post_build_variant is not None:
            serialized = ARObject._serialize_item(self.post_build_variant, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("POST-BUILD-VARIANT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucModuleConfigurationValues":
        """Deserialize XML element to EcucModuleConfigurationValues object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucModuleConfigurationValues object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucModuleConfigurationValues, cls).deserialize(element)

        # Parse containers (list from container "CONTAINERS")
        obj.containers = []
        container = ARObject._find_child_element(element, "CONTAINERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.containers.append(child_value)

        # Parse definition
        child = ARObject._find_child_element(element, "DEFINITION")
        if child is not None:
            definition_value = ARObject._deserialize_by_tag(child, "EcucModuleDef")
            obj.definition = definition_value

        # Parse ecuc_def_edition
        child = ARObject._find_child_element(element, "ECUC-DEF-EDITION")
        if child is not None:
            ecuc_def_edition_value = child.text
            obj.ecuc_def_edition = ecuc_def_edition_value

        # Parse implementation
        child = ARObject._find_child_element(element, "IMPLEMENTATION")
        if child is not None:
            implementation_value = child.text
            obj.implementation = implementation_value

        # Parse module
        child = ARObject._find_child_element(element, "MODULE")
        if child is not None:
            module_value = ARObject._deserialize_by_tag(child, "BswImplementation")
            obj.module = module_value

        # Parse post_build_variant
        child = ARObject._find_child_element(element, "POST-BUILD-VARIANT")
        if child is not None:
            post_build_variant_value = child.text
            obj.post_build_variant = post_build_variant_value

        return obj



class EcucModuleConfigurationValuesBuilder:
    """Builder for EcucModuleConfigurationValues."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucModuleConfigurationValues = EcucModuleConfigurationValues()

    def build(self) -> EcucModuleConfigurationValues:
        """Build and return EcucModuleConfigurationValues object.

        Returns:
            EcucModuleConfigurationValues instance
        """
        # TODO: Add validation
        return self._obj
