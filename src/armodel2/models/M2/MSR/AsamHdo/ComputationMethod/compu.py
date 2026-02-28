"""Compu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 386)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import (
    CompuConst,
)
from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_content import (
    CompuContent,
)
from armodel2.serialization.name_converter import NameConverter
from armodel2.serialization.model_factory import ModelFactory


class Compu(ARObject):
    """AUTOSAR Compu."""

    _XML_TAG = "COMPU"

    _DESERIALIZE_DISPATCH = {}  # Polymorphic content handled by ModelFactory in deserialize

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compu_content: Optional[CompuContent]
    compu_default: Optional[CompuConst]
    def __init__(self) -> None:
        """Initialize Compu."""
        super().__init__()
        self.compu_content: Optional[CompuContent] = None
        self.compu_default: Optional[CompuConst] = None

    def serialize(self) -> ET.Element:
        """Serialize Compu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this Compu
        """
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes (checksum, timestamp)
        parent_elem = super(Compu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize compu_content
        if self.compu_content is not None:
            serialized = SerializationHelper.serialize_item(self.compu_content, "CompuContent")
            if serialized is not None:
                elem.append(serialized)

        # Serialize compu_default
        if self.compu_default is not None:
            serialized = SerializationHelper.serialize_item(self.compu_default, "CompuConst")
            if serialized is not None:
                elem.append(serialized)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Compu":
        """Deserialize XML element to Compu.

        Handles CompuContent polymorphic types by using ModelFactory to resolve
        concrete subclasses like CompuScales. This ensures Compu.compu_content
        is properly populated with the correct concrete subclass.
        Calls super().deserialize() first to handle inherited attributes from ARObject.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Compu instance with compu_content properly set
        """
        # First, deserialize inherited attributes from parent chain (ARObject)
        obj = super(Compu, cls).deserialize(element)

        # Use ModelFactory for polymorphic type resolution
        factory = ModelFactory()
        if not factory.is_initialized():
            factory.load_mappings()

        # Find child elements that are CompuContent or CompuConst subclasses
        ns_split = '}'
        for child in element:
            child_tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            concrete_class = factory.get_class(child_tag)

            if concrete_class:
                # Import base classes for type checking
                from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_content import CompuContent
                from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import CompuConst

                # Check if it's a CompuContent subclass (for compu_content)
                if isinstance(concrete_class, type) and issubclass(concrete_class, CompuContent):
                    obj.compu_content = SerializationHelper.unwrap_primitive(concrete_class.deserialize(child))
                # Check if it's a CompuConst (for compu_default)
                elif isinstance(concrete_class, type) and issubclass(concrete_class, CompuConst):
                    obj.compu_default = SerializationHelper.unwrap_primitive(concrete_class.deserialize(child))

        return obj


class CompuBuilder:
    """Builder for Compu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Compu = Compu()

    def build(self) -> Compu:
        """Build and return Compu object.

        Returns:
            Compu instance
        """
        # TODO: Add validation
        return self._obj
