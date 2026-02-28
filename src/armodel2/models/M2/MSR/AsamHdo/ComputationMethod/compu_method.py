"""CompuMethod AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 308)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 380)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2010)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 436)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 30)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 176)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

if TYPE_CHECKING:
    from typing_extensions import Self

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DisplayFormatString,
)
from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu import (
    Compu,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import (
    ARRef,
)
from armodel2.serialization import SerializationHelper


class CompuMethod(ARElement):
    """AUTOSAR CompuMethod."""

    _XML_TAG = "COMPU-METHOD"

    _DESERIALIZE_DISPATCH = {
        "COMPU-INTERNAL-TO-PHYS": lambda obj, elem: setattr(
            obj, '_compu_internal_to_phys', CompuMethod._deserialize_compu_content(elem)
        ),
        "COMPU-PHYS-TO-INTERNAL": lambda obj, elem: setattr(
            obj, '_compu_phys_to_internal', CompuMethod._deserialize_compu_content(elem)
        ),
        "DISPLAY-FORMAT": lambda obj, elem: setattr(
            obj, 'display_format', elem.text
        ),
        "UNIT-REF": lambda obj, elem: setattr(
            obj, 'unit', ARRef.deserialize(elem)
        ),
    }

    compu_internal_to_phys: Optional[Compu]
    compu_phys_to_internal: Optional[Compu]
    display_format: Optional[DisplayFormatString]
    unit: Optional[ARRef]

    @staticmethod
    def _deserialize_compu_content(elem: ET.Element) -> Compu:
        """Helper to deserialize Compu content from wrapper element."""
        from armodel2.serialization import SerializationHelper
        from armodel2.serialization.model_factory import ModelFactory
        from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_content import CompuContent
        from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import CompuConst

        compu_obj = Compu()
        factory = ModelFactory()
        if not factory.is_initialized():
            factory.load_mappings()

        for child in elem:
            child_tag = SerializationHelper.strip_namespace(child.tag)
            concrete_class = factory.get_class(child_tag)

            if concrete_class:
                if isinstance(concrete_class, type) and issubclass(concrete_class, CompuContent):
                    compu_obj.compu_content = SerializationHelper.unwrap_primitive(concrete_class.deserialize(child))
                elif isinstance(concrete_class, type) and issubclass(concrete_class, CompuConst):
                    compu_obj.compu_default = SerializationHelper.unwrap_primitive(concrete_class.deserialize(child))

        return compu_obj

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize CompuMethod."""
        super().__init__()
        self._compu_internal_to_phys: Optional[Compu] = None
        self._compu_phys_to_internal: Optional[Compu] = None
        self.display_format: Optional[DisplayFormatString] = None
        self.unit: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize CompuMethod to XML element.

        Handles custom serialization for Compu objects by directly
        serializing them without creating additional wrapper tags.

        Returns:
            xml.etree.ElementTree.Element representing this CompuMethod
        """
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CompuMethod, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize unit (UNIT-REF is a reference, not a UNIT element)
        # Must come before COMPU-INTERNAL-TO-PHYS to match original XML order
        if self.unit is not None:
            serialized = SerializationHelper.serialize_item(self.unit, "ARRef")
            if serialized is not None:
                # ARRef.serialize() returns a generic element, we need to set the correct tag
                serialized.tag = "UNIT-REF"
                elem.append(serialized)

        # Serialize compu_internal_to_phys as COMPU-INTERNAL-TO-PHYS element
        if self._compu_internal_to_phys is not None:
            compu_elem = self._compu_internal_to_phys.serialize()
            # The Compu.serialize() returns a <COMPU> element, but we need to wrap it
            # in <COMPU-INTERNAL-TO-PHYS>. The Compu element's children should be copied
            # to the wrapper element.
            wrapper = ET.Element("COMPU-INTERNAL-TO-PHYS")
            # Copy all children from the serialized Compu to the wrapper
            for child in list(compu_elem):
                wrapper.append(child)
            elem.append(wrapper)

        # Serialize compu_phys_to_internal as COMPU-PHYS-TO-INTERNAL element
        if self._compu_phys_to_internal is not None:
            compu_elem = self._compu_phys_to_internal.serialize()
            # Same logic as compu_internal_to_phys
            wrapper = ET.Element("COMPU-PHYS-TO-INTERNAL")
            for child in list(compu_elem):
                wrapper.append(child)
            elem.append(wrapper)

        # Serialize display_format
        if self.display_format is not None:
            serialized = SerializationHelper.serialize_item(self.display_format, "DisplayFormatString")
            if serialized is not None:
                elem.append(serialized)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element):
        """Deserialize XML element to CompuMethod.

        Uses static dispatch table for O(1) tag-to-handler lookup.
        Handles the COMPU-INTERNAL-TO-PHYS and COMPU-PHYS-TO-INTERNAL elements
        by using the factory pattern to properly deserialize them as Compu objects.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuMethod instance
        """
        obj = cls.__new__(cls)
        obj.__init__()

        # Single-pass deserialization with dispatch table
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            handler = cls._DESERIALIZE_DISPATCH.get(tag)
            if handler is not None:
                handler(obj, child)

        return obj

    @property
    def compu_internal_to_phys(self) -> Optional[Compu]:
        """Get compu_internal_to_phys value."""
        return self._compu_internal_to_phys

    @compu_internal_to_phys.setter
    def compu_internal_to_phys(self, value: Optional[Compu]) -> None:
        """Set compu_internal_to_phys value."""
        self._compu_internal_to_phys = value

    @property
    def compu_phys_to_internal(self) -> Optional[Compu]:
        """Get compu_phys_to_internal value."""
        return self._compu_phys_to_internal

    @compu_phys_to_internal.setter
    def compu_phys_to_internal(self, value: Optional[Compu]) -> None:
        """Set compu_phys_to_internal value."""
        self._compu_phys_to_internal = value


class CompuMethodBuilder:
    """Builder for CompuMethod."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuMethod = CompuMethod()

    def build(self) -> CompuMethod:
        """Build and return CompuMethod object.

        Returns:
            CompuMethod instance
        """
        # TODO: Add validation
        return self._obj
