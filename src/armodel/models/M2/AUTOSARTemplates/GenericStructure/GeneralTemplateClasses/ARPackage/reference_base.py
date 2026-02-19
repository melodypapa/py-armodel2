"""ReferenceBase AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 72)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ARPackage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    ReferrableSubtypesEnum,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
        ARPackage,
    )



class ReferenceBase(ARObject):
    """AUTOSAR ReferenceBase."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    global_element_refs: list[ARRef]
    global_ins: list[ARPackage]
    is_default: Boolean
    package: Optional[ARPackage]
    short_label: Identifier
    def __init__(self) -> None:
        """Initialize ReferenceBase."""
        super().__init__()
        self.global_element_refs: list[ARRef] = []
        self.global_ins: list[ARPackage] = []
        self.is_default: Boolean = None
        self.package: Optional[ARPackage] = None
        self.short_label: Identifier = None
    def serialize(self) -> ET.Element:
        """Serialize ReferenceBase to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize global_element_refs (list to container "GLOBAL-ELEMENTS")
        if self.global_element_refs:
            wrapper = ET.Element("GLOBAL-ELEMENTS")
            for item in self.global_element_refs:
                serialized = ARObject._serialize_item(item, "ReferrableSubtypesEnum")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize global_ins (list to container "GLOBAL-INS")
        if self.global_ins:
            wrapper = ET.Element("GLOBAL-INS")
            for item in self.global_ins:
                serialized = ARObject._serialize_item(item, "ARPackage")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize is_default
        if self.is_default is not None:
            serialized = ARObject._serialize_item(self.is_default, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize package
        if self.package is not None:
            serialized = ARObject._serialize_item(self.package, "ARPackage")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PACKAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_label
        if self.short_label is not None:
            serialized = ARObject._serialize_item(self.short_label, "Identifier")
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
    def deserialize(cls, element: ET.Element) -> "ReferenceBase":
        """Deserialize XML element to ReferenceBase object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReferenceBase object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse global_element_refs (list from container "GLOBAL-ELEMENTS")
        obj.global_element_refs = []
        container = ARObject._find_child_element(element, "GLOBAL-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.global_element_refs.append(child_value)

        # Parse global_ins (list from container "GLOBAL-INS")
        obj.global_ins = []
        container = ARObject._find_child_element(element, "GLOBAL-INS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.global_ins.append(child_value)

        # Parse is_default
        child = ARObject._find_child_element(element, "IS-DEFAULT")
        if child is not None:
            is_default_value = child.text
            obj.is_default = is_default_value

        # Parse package
        child = ARObject._find_child_element(element, "PACKAGE")
        if child is not None:
            package_value = ARObject._deserialize_by_tag(child, "ARPackage")
            obj.package = package_value

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        return obj



class ReferenceBaseBuilder:
    """Builder for ReferenceBase."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceBase = ReferenceBase()

    def build(self) -> ReferenceBase:
        """Build and return ReferenceBase object.

        Returns:
            ReferenceBase instance
        """
        # TODO: Add validation
        return self._obj
