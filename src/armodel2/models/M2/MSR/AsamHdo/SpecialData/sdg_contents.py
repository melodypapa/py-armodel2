"""SdgContents AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 90)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json

NOTE: This file is manually maintained to properly handle the atp_mixed pattern
where multiple SD/SDF/SDG children can appear under SDG.
The attributes use LIST types to support multiple children of the same type.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_mixed

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sd import (
    Sd,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdf import (
    Sdf,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdg import (
        Sdg,
    )

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper

@atp_mixed()
class SdgContents(ARObject):
    """AUTOSAR SdgContents.

    The SdgContents class uses the atp_mixed pattern where its children
    serialize directly under the parent SDG element without a wrapper.

    This implementation uses LIST attributes to support multiple children
    of the same type (e.g., multiple SD elements under a single SDG).

    Attributes:
        sd: List of SD elements
        sdf: List of SDF elements
        sdg: List of nested SDG elements
        sdx_ref: List of SDX-REF elements (polymorphic references)
        sdxf_ref: List of SDXF-REF elements (polymorphic references)
    """

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SDG-CONTENTS"

    # Use LIST attributes to support multiple children
    sd: List[Sd]
    sdf: List[Sdf]
    sdg: List[Sdg]
    sdx_ref: List[ARRef]
    sdxf_ref: List[ARRef]

    def __init__(self) -> None:
        """Initialize SdgContents."""
        super().__init__()
        self.sd: List[Sd] = []
        self.sdf: List[Sdf] = []
        self.sdg: List[Sdg] = []
        self.sdx_ref: List[ARRef] = []
        self.sdxf_ref: List[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize SdgContents to XML element (atp_mixed - children serialize directly).

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgContents, self).serialize()

        # Copy all attributes from parent element to current element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to current element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element to current element
        for child in parent_elem:
            elem.append(child)

        # Serialize all SD elements
        for sd_item in self.sd:
            serialized = SerializationHelper.serialize_item(sd_item, "Sd")
            if serialized is not None:
                wrapped = ET.Element("SD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize all SDF elements
        for sdf_item in self.sdf:
            serialized = SerializationHelper.serialize_item(sdf_item, "Sdf")
            if serialized is not None:
                wrapped = ET.Element("SDF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize all nested SDG elements
        for sdg_item in self.sdg:
            serialized = SerializationHelper.serialize_item(sdg_item, "Sdg")
            if serialized is not None:
                wrapped = ET.Element("SDG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize all SDX-REF elements
        for sdx_ref_item in self.sdx_ref:
            serialized = SerializationHelper.serialize_item(sdx_ref_item, "ARRef")
            if serialized is not None:
                wrapped = ET.Element("SDX-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize all SDXF-REF elements
        for sdxf_ref_item in self.sdxf_ref:
            serialized = SerializationHelper.serialize_item(sdxf_ref_item, "ARRef")
            if serialized is not None:
                wrapped = ET.Element("SDXF-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> SdgContents:
        """Deserialize XML element to SdgContents object (atp_mixed - children serialize directly).

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgContents object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgContents, cls).deserialize(element)

        # Initialize lists
        obj.sd = []
        obj.sdf = []
        obj.sdg = []
        obj.sdx_ref = []
        obj.sdxf_ref = []

        # Deserialize children
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SD":
                obj.sd.append(SerializationHelper.deserialize_by_tag(child, "Sd"))
            elif tag == "SDF":
                obj.sdf.append(SerializationHelper.deserialize_by_tag(child, "Sdf"))
            elif tag == "SDG":
                obj.sdg.append(SerializationHelper.deserialize_by_tag(child, "Sdg"))
            elif tag == "SDX-REF":
                obj.sdx_ref.append(SerializationHelper.deserialize_by_tag(child, "ARRef"))
            elif tag == "SDXF-REF":
                obj.sdxf_ref.append(SerializationHelper.deserialize_by_tag(child, "ARRef"))

        return obj


class SdgContentsBuilder(BuilderBase):
    """Builder for SdgContents with fluent API."""

    def __init__(self) -> None:
        """Initialize SdgContentsBuilder."""
        self._instance: Optional[SdgContents] = None

    def _get_instance(self) -> SdgContents:
        """Get or create the SdgContents instance."""
        if self._instance is None:
            self._instance = SdgContents()
        return self._instance

    def with_sd(self, sd: Optional[List[Sd]]) -> "SdgContentsBuilder":
        """Set the sd list attribute.

        Args:
            sd: List of Sd values

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        if sd is not None:
            obj.sd = sd
        return self

    def add_sd(self, sd: Sd) -> "SdgContentsBuilder":
        """Add an SD element to the list.

        Args:
            sd: Sd value to add

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sd.append(sd)
        return self

    def clear_sd(self) -> "SdgContentsBuilder":
        """Clear the SD list.

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sd.clear()
        return self

    def with_sdf(self, sdf: Optional[List[Sdf]]) -> "SdgContentsBuilder":
        """Set the sdf list attribute.

        Args:
            sdf: List of Sdf values

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        if sdf is not None:
            obj.sdf = sdf
        return self

    def add_sdf(self, sdf: Sdf) -> "SdgContentsBuilder":
        """Add an SDF element to the list.

        Args:
            sdf: Sdf value to add

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sdf.append(sdf)
        return self

    def clear_sdf(self) -> "SdgContentsBuilder":
        """Clear the SDF list.

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sdf.clear()
        return self

    def with_sdg(self, sdg: Optional[List["Sdg"]]) -> "SdgContentsBuilder":
        """Set the sdg list attribute.

        Args:
            sdg: List of Sdg values

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        if sdg is not None:
            obj.sdg = sdg
        return self

    def add_sdg(self, sdg: "Sdg") -> "SdgContentsBuilder":
        """Add an SDG element to the list.

        Args:
            sdg: Sdg value to add

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sdg.append(sdg)
        return self

    def clear_sdg(self) -> "SdgContentsBuilder":
        """Clear the SDG list.

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sdg.clear()
        return self

    def with_sdx_ref(self, sdx_ref: Optional[List[ARRef]]) -> "SdgContentsBuilder":
        """Set the sdx_ref list attribute.

        Args:
            sdx_ref: List of ARRef values

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        if sdx_ref is not None:
            obj.sdx_ref = sdx_ref
        return self

    def add_sdx_ref(self, sdx_ref: ARRef) -> "SdgContentsBuilder":
        """Add an SDX-REF element to the list.

        Args:
            sdx_ref: ARRef value to add

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sdx_ref.append(sdx_ref)
        return self

    def clear_sdx_ref(self) -> "SdgContentsBuilder":
        """Clear the SDX-REF list.

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sdx_ref.clear()
        return self

    def with_sdxf_ref(self, sdxf_ref: Optional[List[ARRef]]) -> "SdgContentsBuilder":
        """Set the sdxf_ref list attribute.

        Args:
            sdxf_ref: List of ARRef values

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        if sdxf_ref is not None:
            obj.sdxf_ref = sdxf_ref
        return self

    def add_sdxf_ref(self, sdxf_ref: ARRef) -> "SdgContentsBuilder":
        """Add an SDXF-REF element to the list.

        Args:
            sdxf_ref: ARRef value to add

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sdxf_ref.append(sdxf_ref)
        return self

    def clear_sdxf_ref(self) -> "SdgContentsBuilder":
        """Clear the SDXF-REF list.

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sdxf_ref.clear()
        return self

    def build(self) -> SdgContents:
        """Build and return the SdgContents object.

        Returns:
            The constructed SdgContents object
        """
        obj = self._get_instance()
        if obj is None:
            obj = SdgContents()
        return obj
