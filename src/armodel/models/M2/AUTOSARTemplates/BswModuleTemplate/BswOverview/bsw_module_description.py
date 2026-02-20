"""BswModuleDescription AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 26)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 303)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 973)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 212)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 426)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 168)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswOverview.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation.sw_component_documentation import (
    SwComponentDocumentation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_dependency import (
        BswModuleDependency,
    )



class BswModuleDescription(ARElement):
    """AUTOSAR BswModuleDescription."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_module_refs: list[ARRef]
    bsw_module_documentation: Optional[SwComponentDocumentation]
    expected_entrie_refs: list[ARRef]
    implemented_refs: list[ARRef]
    internal_behaviors: list[BswInternalBehavior]
    module_id: Optional[PositiveInteger]
    provided_clients: list[BswModuleClientServerEntry]
    provided_data_refs: list[ARRef]
    provided_mode_refs: list[ARRef]
    released_trigger_refs: list[ARRef]
    required_clients: list[BswModuleClientServerEntry]
    required_data_refs: list[ARRef]
    required_mode_refs: list[ARRef]
    required_trigger_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize BswModuleDescription."""
        super().__init__()
        self.bsw_module_refs: list[ARRef] = []
        self.bsw_module_documentation: Optional[SwComponentDocumentation] = None
        self.expected_entrie_refs: list[ARRef] = []
        self.implemented_refs: list[ARRef] = []
        self.internal_behaviors: list[BswInternalBehavior] = []
        self.module_id: Optional[PositiveInteger] = None
        self.provided_clients: list[BswModuleClientServerEntry] = []
        self.provided_data_refs: list[ARRef] = []
        self.provided_mode_refs: list[ARRef] = []
        self.released_trigger_refs: list[ARRef] = []
        self.required_clients: list[BswModuleClientServerEntry] = []
        self.required_data_refs: list[ARRef] = []
        self.required_mode_refs: list[ARRef] = []
        self.required_trigger_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize BswModuleDescription to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModuleDescription, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_module_refs (list to container "BSW-MODULE-REFS")
        if self.bsw_module_refs:
            wrapper = ET.Element("BSW-MODULE-REFS")
            for item in self.bsw_module_refs:
                serialized = ARObject._serialize_item(item, "BswModuleDependency")
                if serialized is not None:
                    child_elem = ET.Element("BSW-MODULE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize bsw_module_documentation
        if self.bsw_module_documentation is not None:
            serialized = ARObject._serialize_item(self.bsw_module_documentation, "SwComponentDocumentation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-MODULE-DOCUMENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize expected_entrie_refs (list to container "EXPECTED-ENTRIE-REFS")
        if self.expected_entrie_refs:
            wrapper = ET.Element("EXPECTED-ENTRIE-REFS")
            for item in self.expected_entrie_refs:
                serialized = ARObject._serialize_item(item, "BswModuleEntry")
                if serialized is not None:
                    child_elem = ET.Element("EXPECTED-ENTRIE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize implemented_refs (list to container "IMPLEMENTED-REFS")
        if self.implemented_refs:
            wrapper = ET.Element("IMPLEMENTED-REFS")
            for item in self.implemented_refs:
                serialized = ARObject._serialize_item(item, "BswModuleEntry")
                if serialized is not None:
                    child_elem = ET.Element("IMPLEMENTED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize internal_behaviors (list to container "INTERNAL-BEHAVIORS")
        if self.internal_behaviors:
            wrapper = ET.Element("INTERNAL-BEHAVIORS")
            for item in self.internal_behaviors:
                serialized = ARObject._serialize_item(item, "BswInternalBehavior")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize module_id
        if self.module_id is not None:
            serialized = ARObject._serialize_item(self.module_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODULE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize provided_clients (list to container "PROVIDED-CLIENTS")
        if self.provided_clients:
            wrapper = ET.Element("PROVIDED-CLIENTS")
            for item in self.provided_clients:
                serialized = ARObject._serialize_item(item, "BswModuleClientServerEntry")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize provided_data_refs (list to container "PROVIDED-DATA-REFS")
        if self.provided_data_refs:
            wrapper = ET.Element("PROVIDED-DATA-REFS")
            for item in self.provided_data_refs:
                serialized = ARObject._serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("PROVIDED-DATA-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize provided_mode_refs (list to container "PROVIDED-MODE-REFS")
        if self.provided_mode_refs:
            wrapper = ET.Element("PROVIDED-MODE-REFS")
            for item in self.provided_mode_refs:
                serialized = ARObject._serialize_item(item, "ModeDeclarationGroup")
                if serialized is not None:
                    child_elem = ET.Element("PROVIDED-MODE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize released_trigger_refs (list to container "RELEASED-TRIGGER-REFS")
        if self.released_trigger_refs:
            wrapper = ET.Element("RELEASED-TRIGGER-REFS")
            for item in self.released_trigger_refs:
                serialized = ARObject._serialize_item(item, "Trigger")
                if serialized is not None:
                    child_elem = ET.Element("RELEASED-TRIGGER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_clients (list to container "REQUIRED-CLIENTS")
        if self.required_clients:
            wrapper = ET.Element("REQUIRED-CLIENTS")
            for item in self.required_clients:
                serialized = ARObject._serialize_item(item, "BswModuleClientServerEntry")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_data_refs (list to container "REQUIRED-DATA-REFS")
        if self.required_data_refs:
            wrapper = ET.Element("REQUIRED-DATA-REFS")
            for item in self.required_data_refs:
                serialized = ARObject._serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("REQUIRED-DATA-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_mode_refs (list to container "REQUIRED-MODE-REFS")
        if self.required_mode_refs:
            wrapper = ET.Element("REQUIRED-MODE-REFS")
            for item in self.required_mode_refs:
                serialized = ARObject._serialize_item(item, "ModeDeclarationGroup")
                if serialized is not None:
                    child_elem = ET.Element("REQUIRED-MODE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_trigger_refs (list to container "REQUIRED-TRIGGER-REFS")
        if self.required_trigger_refs:
            wrapper = ET.Element("REQUIRED-TRIGGER-REFS")
            for item in self.required_trigger_refs:
                serialized = ARObject._serialize_item(item, "Trigger")
                if serialized is not None:
                    child_elem = ET.Element("REQUIRED-TRIGGER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleDescription":
        """Deserialize XML element to BswModuleDescription object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModuleDescription object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModuleDescription, cls).deserialize(element)

        # Parse bsw_module_refs (list from container "BSW-MODULE-REFS")
        obj.bsw_module_refs = []
        container = ARObject._find_child_element(element, "BSW-MODULE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.bsw_module_refs.append(child_value)

        # Parse bsw_module_documentation
        child = ARObject._find_child_element(element, "BSW-MODULE-DOCUMENTATION")
        if child is not None:
            bsw_module_documentation_value = ARObject._deserialize_by_tag(child, "SwComponentDocumentation")
            obj.bsw_module_documentation = bsw_module_documentation_value

        # Parse expected_entrie_refs (list from container "EXPECTED-ENTRIE-REFS")
        obj.expected_entrie_refs = []
        container = ARObject._find_child_element(element, "EXPECTED-ENTRIE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.expected_entrie_refs.append(child_value)

        # Parse implemented_refs (list from container "IMPLEMENTED-REFS")
        obj.implemented_refs = []
        container = ARObject._find_child_element(element, "IMPLEMENTED-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.implemented_refs.append(child_value)

        # Parse internal_behaviors (list from container "INTERNAL-BEHAVIORS")
        obj.internal_behaviors = []
        container = ARObject._find_child_element(element, "INTERNAL-BEHAVIORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.internal_behaviors.append(child_value)

        # Parse module_id
        child = ARObject._find_child_element(element, "MODULE-ID")
        if child is not None:
            module_id_value = child.text
            obj.module_id = module_id_value

        # Parse provided_clients (list from container "PROVIDED-CLIENTS")
        obj.provided_clients = []
        container = ARObject._find_child_element(element, "PROVIDED-CLIENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_clients.append(child_value)

        # Parse provided_data_refs (list from container "PROVIDED-DATA-REFS")
        obj.provided_data_refs = []
        container = ARObject._find_child_element(element, "PROVIDED-DATA-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_data_refs.append(child_value)

        # Parse provided_mode_refs (list from container "PROVIDED-MODE-REFS")
        obj.provided_mode_refs = []
        container = ARObject._find_child_element(element, "PROVIDED-MODE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_mode_refs.append(child_value)

        # Parse released_trigger_refs (list from container "RELEASED-TRIGGER-REFS")
        obj.released_trigger_refs = []
        container = ARObject._find_child_element(element, "RELEASED-TRIGGER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.released_trigger_refs.append(child_value)

        # Parse required_clients (list from container "REQUIRED-CLIENTS")
        obj.required_clients = []
        container = ARObject._find_child_element(element, "REQUIRED-CLIENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_clients.append(child_value)

        # Parse required_data_refs (list from container "REQUIRED-DATA-REFS")
        obj.required_data_refs = []
        container = ARObject._find_child_element(element, "REQUIRED-DATA-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_data_refs.append(child_value)

        # Parse required_mode_refs (list from container "REQUIRED-MODE-REFS")
        obj.required_mode_refs = []
        container = ARObject._find_child_element(element, "REQUIRED-MODE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_mode_refs.append(child_value)

        # Parse required_trigger_refs (list from container "REQUIRED-TRIGGER-REFS")
        obj.required_trigger_refs = []
        container = ARObject._find_child_element(element, "REQUIRED-TRIGGER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_trigger_refs.append(child_value)

        return obj



class BswModuleDescriptionBuilder:
    """Builder for BswModuleDescription."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleDescription = BswModuleDescription()

    def build(self) -> BswModuleDescription:
        """Build and return BswModuleDescription object.

        Returns:
            BswModuleDescription instance
        """
        # TODO: Add validation
        return self._obj
