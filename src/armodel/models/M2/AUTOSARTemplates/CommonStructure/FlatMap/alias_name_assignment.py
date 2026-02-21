"""AliasNameAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 175)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 968)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)


class AliasNameAssignment(ARObject):
    """AUTOSAR AliasNameAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    flat_instance_ref: Optional[ARRef]
    identifiable_ref: Optional[ARRef]
    label: Optional[MultilanguageLongName]
    short_label: Optional[String]
    def __init__(self) -> None:
        """Initialize AliasNameAssignment."""
        super().__init__()
        self.flat_instance_ref: Optional[ARRef] = None
        self.identifiable_ref: Optional[ARRef] = None
        self.label: Optional[MultilanguageLongName] = None
        self.short_label: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize AliasNameAssignment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize flat_instance_ref
        if self.flat_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.flat_instance_ref, "FlatInstanceDescriptor")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLAT-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize identifiable_ref
        if self.identifiable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.identifiable_ref, "Identifiable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENTIFIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize label
        if self.label is not None:
            serialized = SerializationHelper.serialize_item(self.label, "MultilanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AliasNameAssignment":
        """Deserialize XML element to AliasNameAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AliasNameAssignment object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse flat_instance_ref
        child = SerializationHelper.find_child_element(element, "FLAT-INSTANCE-REF")
        if child is not None:
            flat_instance_ref_value = ARRef.deserialize(child)
            obj.flat_instance_ref = flat_instance_ref_value

        # Parse identifiable_ref
        child = SerializationHelper.find_child_element(element, "IDENTIFIABLE-REF")
        if child is not None:
            identifiable_ref_value = ARRef.deserialize(child)
            obj.identifiable_ref = identifiable_ref_value

        # Parse label
        child = SerializationHelper.find_child_element(element, "LABEL")
        if child is not None:
            label_value = SerializationHelper.deserialize_with_type(child, "MultilanguageLongName")
            obj.label = label_value

        # Parse short_label
        child = SerializationHelper.find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = child.text
            obj.short_label = short_label_value

        return obj



class AliasNameAssignmentBuilder:
    """Builder for AliasNameAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AliasNameAssignment = AliasNameAssignment()

    def build(self) -> AliasNameAssignment:
        """Build and return AliasNameAssignment object.

        Returns:
            AliasNameAssignment instance
        """
        # TODO: Add validation
        return self._obj
