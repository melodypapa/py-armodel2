"""DataPrototypeGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 223)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 180)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class DataPrototypeGroup(Identifiable):
    """AUTOSAR DataPrototypeGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_prototype_group_group_in_composition_instance_ref_refs: list[ARRef]
    implicit_data_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize DataPrototypeGroup."""
        super().__init__()
        self.data_prototype_group_group_in_composition_instance_ref_refs: list[ARRef] = []
        self.implicit_data_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototypeGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_prototype_group_group_in_composition_instance_ref_refs (list to container "DATA-PROTOTYPE-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REF-REFS")
        if self.data_prototype_group_group_in_composition_instance_ref_refs:
            wrapper = ET.Element("DATA-PROTOTYPE-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REF-REFS")
            for item in self.data_prototype_group_group_in_composition_instance_ref_refs:
                serialized = SerializationHelper.serialize_item(item, "DataPrototypeGroup")
                if serialized is not None:
                    child_elem = ET.Element("DATA-PROTOTYPE-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REF-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize implicit_data_refs (list to container "IMPLICIT-DATA-REFS")
        if self.implicit_data_refs:
            wrapper = ET.Element("IMPLICIT-DATA-REFS")
            for item in self.implicit_data_refs:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("IMPLICIT-DATA-REF")
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
    def deserialize(cls, element: ET.Element) -> "DataPrototypeGroup":
        """Deserialize XML element to DataPrototypeGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototypeGroup, cls).deserialize(element)

        # Parse data_prototype_group_group_in_composition_instance_ref_refs (list from container "DATA-PROTOTYPE-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REF-REFS")
        obj.data_prototype_group_group_in_composition_instance_ref_refs = []
        container = SerializationHelper.find_child_element(element, "DATA-PROTOTYPE-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REF-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_prototype_group_group_in_composition_instance_ref_refs.append(child_value)

        # Parse implicit_data_refs (list from container "IMPLICIT-DATA-REFS")
        obj.implicit_data_refs = []
        container = SerializationHelper.find_child_element(element, "IMPLICIT-DATA-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.implicit_data_refs.append(child_value)

        return obj



class DataPrototypeGroupBuilder:
    """Builder for DataPrototypeGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeGroup = DataPrototypeGroup()

    def build(self) -> DataPrototypeGroup:
        """Build and return DataPrototypeGroup object.

        Returns:
            DataPrototypeGroup instance
        """
        # TODO: Add validation
        return self._obj
