"""Sdg AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 328)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1004)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 78)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 90)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json

NOTE: This file is manually maintained to properly handle the atp_mixed pattern
where multiple SD/SDF/SDG/SDX/SDXF children can appear under SDG.
The sdg_contents_type attribute stores SdgContents, whose children serialize
directly under SDG (atp_mixed pattern).
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import xml_attribute

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sd import (
    Sd,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdf import (
    Sdf,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdg_caption import (
    SdgCaption,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdg_contents import (
        SdgContents,
    )

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Sdg(ARObject):
    """AUTOSAR Sdg.

    The Sdg class represents special data groups in AUTOSAR. It uses the
    atp_mixed pattern where the SdgContents children serialize directly
    under the SDG element without a wrapper.

    Attributes:
        gid: The GID attribute (group identifier)
        sdg_caption: Optional caption for the SDG
        sdg_contents_type: Container for SD/SDF/SDG/SDX/SDXF children (atp_mixed)
    """

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SDG"

    # Legacy single-value attributes (kept for backward compatibility)
    # These are set to the first child element during deserialization
    sd: Optional[Sd]
    sdf: Optional[Sdf]
    sdg: Optional["Sdg"]
    sdx: Optional[Referrable]
    sdxf: Optional[Referrable]

    # Primary attribute for atp_mixed content
    # SdgContents uses @atp_mixed decorator, so its children serialize directly
    sdg_contents_type: Optional["SdgContents"]

    def __init__(self) -> None:
        """Initialize Sdg."""
        super().__init__()
        self._gid: NameToken = None
        self.sdg_caption: Optional[SdgCaption] = None
        # Legacy single-value attributes
        self.sd: Optional[Sd] = None
        self.sdf: Optional[Sdf] = None
        self.sdg: Optional[Sdg] = None
        self.sdx: Optional[Referrable] = None
        self.sdxf: Optional[Referrable] = None
        # Primary atp_mixed container
        self.sdg_contents_type: Optional[SdgContents] = None

    @property
    @xml_attribute
    def gid(self) -> NameToken:
        """Get gid XML attribute."""
        return self._gid

    @gid.setter
    def gid(self, value: NameToken) -> None:
        """Set gid XML attribute."""
        self._gid = value

    def serialize(self) -> ET.Element:
        """Serialize Sdg to XML element.

        The atp_mixed pattern means that SdgContents children serialize
        directly under the SDG element without a wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Sdg, self).serialize()
        elem.attrib.update(parent_elem.attrib)
        if parent_elem.text:
            elem.text = parent_elem.text
        for child in parent_elem:
            elem.append(child)

        # Serialize gid as XML attribute
        if self.gid is not None:
            elem.attrib["GID"] = str(self.gid)

        # Serialize sdg_caption
        if self.sdg_caption is not None:
            serialized = SerializationHelper.serialize_item(self.sdg_caption, "SdgCaption")
            if serialized is not None:
                wrapped = ET.Element("SDG-CAPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdg_contents_type (atp_mixed pattern)
        # When SdgContents is set, its children serialize directly under SDG
        if self.sdg_contents_type is not None:
            # Serialize the SdgContents and append its children directly
            serialized = self.sdg_contents_type.serialize()
            # For atp_mixed, append children directly, not the wrapper element
            for child in serialized:
                elem.append(child)
        else:
            # Fallback to legacy single-value attributes for backward compatibility
            if self.sd is not None:
                serialized = SerializationHelper.serialize_item(self.sd, "Sd")
                if serialized is not None:
                    wrapped = ET.Element("SD")
                    if hasattr(serialized, 'attrib'):
                        wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                    for child in serialized:
                        wrapped.append(child)
                    elem.append(wrapped)

            if self.sdf is not None:
                serialized = SerializationHelper.serialize_item(self.sdf, "Sdf")
                if serialized is not None:
                    wrapped = ET.Element("SDF")
                    if hasattr(serialized, 'attrib'):
                        wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                    for child in serialized:
                        wrapped.append(child)
                    elem.append(wrapped)

            if self.sdg is not None:
                serialized = SerializationHelper.serialize_item(self.sdg, "Sdg")
                if serialized is not None:
                    wrapped = ET.Element("SDG")
                    if hasattr(serialized, 'attrib'):
                        wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                    for child in serialized:
                        wrapped.append(child)
                    elem.append(wrapped)

            if self.sdx is not None:
                serialized = SerializationHelper.serialize_item(self.sdx, "Referrable")
                if serialized is not None:
                    wrapped = ET.Element("SDX")
                    if hasattr(serialized, 'attrib'):
                        wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                    for child in serialized:
                        wrapped.append(child)
                    elem.append(wrapped)

            if self.sdxf is not None:
                serialized = SerializationHelper.serialize_item(self.sdxf, "Referrable")
                if serialized is not None:
                    wrapped = ET.Element("SDXF")
                    if hasattr(serialized, 'attrib'):
                        wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                    for child in serialized:
                        wrapped.append(child)
                    elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Sdg":
        """Deserialize XML element to Sdg object.

        Collects all SD/SDF/SDG/SDX/SDXF children into SdgContents for
        proper handling of multiple children of the same type.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Sdg object
        """
        from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdg_contents import SdgContents

        # First, call parent's deserialize to handle inherited attributes
        obj = super(Sdg, cls).deserialize(element)

        # Parse gid from XML attribute
        if "GID" in element.attrib:
            obj.gid = element.attrib["GID"]

        # Collect SD/SDF/SDG/SDX/SDXF children for atp_mixed handling
        sd_children: List[ET.Element] = []
        sdf_children: List[ET.Element] = []
        sdg_children: List[ET.Element] = []
        sdx_children: List[ET.Element] = []
        sdxf_children: List[ET.Element] = []

        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SDG-CAPTION":
                setattr(obj, "sdg_caption", SerializationHelper.deserialize_by_tag(child, "SdgCaption"))
            elif tag == "SD":
                sd_children.append(child)
            elif tag == "SDF":
                sdf_children.append(child)
            elif tag == "SDG":
                sdg_children.append(child)
            elif tag == "SDX":
                sdx_children.append(child)
            elif tag == "SDXF":
                sdxf_children.append(child)

        # If we have any children, create SdgContents to hold them
        if sd_children or sdf_children or sdg_children or sdx_children or sdxf_children:
            obj.sdg_contents_type = SdgContents()

            # Deserialize ALL children into SdgContents lists
            for sd_child in sd_children:
                obj.sdg_contents_type.sd.append(SerializationHelper.deserialize_by_tag(sd_child, "Sd"))
            # Also set legacy attribute for backward compatibility (first element)
            if obj.sdg_contents_type.sd:
                obj.sd = obj.sdg_contents_type.sd[0]

            for sdf_child in sdf_children:
                obj.sdg_contents_type.sdf.append(SerializationHelper.deserialize_by_tag(sdf_child, "Sdf"))
            if obj.sdg_contents_type.sdf:
                obj.sdf = obj.sdg_contents_type.sdf[0]

            for sdg_child in sdg_children:
                obj.sdg_contents_type.sdg.append(SerializationHelper.deserialize_by_tag(sdg_child, "Sdg"))
            if obj.sdg_contents_type.sdg:
                obj.sdg = obj.sdg_contents_type.sdg[0]

            # For SDX/SDXF: handle polymorphic references
            for sdx_child in sdx_children:
                obj.sdg_contents_type.sdx_ref.append(SerializationHelper.deserialize_by_tag(sdx_child, "ARRef"))
            if obj.sdg_contents_type.sdx_ref:
                obj.sdx = obj.sdg_contents_type.sdx_ref[0]

            for sdxf_child in sdxf_children:
                obj.sdg_contents_type.sdxf_ref.append(SerializationHelper.deserialize_by_tag(sdxf_child, "ARRef"))
            if obj.sdg_contents_type.sdxf_ref:
                obj.sdxf = obj.sdg_contents_type.sdxf_ref[0]

        return obj


class SdgBuilder(BuilderBase):
    """Builder for Sdg objects."""

    def __init__(self) -> None:
        """Initialize SdgBuilder."""
        self._instance: Optional[Sdg] = None

    def _get_instance(self) -> Sdg:
        """Get or create the Sdg instance."""
        if self._instance is None:
            self._instance = Sdg()
        return self._instance

    def with_gid(self, gid: NameToken) -> "SdgBuilder":
        """Set the GID attribute.

        Args:
            gid: Group identifier value

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.gid = gid
        return self

    def with_sdg_caption(self, sdg_caption: Optional[SdgCaption]) -> "SdgBuilder":
        """Set the sdg_caption attribute.

        Args:
            sdg_caption: SdgCaption value

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sdg_caption = sdg_caption
        return self

    def with_sdg_contents_type(self, sdg_contents_type: Optional["SdgContents"]) -> "SdgBuilder":
        """Set the sdg_contents_type attribute.

        Args:
            sdg_contents_type: SdgContents value

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sdg_contents_type = sdg_contents_type
        return self

    def with_sd(self, sd: Optional[Sd]) -> "SdgBuilder":
        """Set the sd attribute (legacy).

        Args:
            sd: Sd value

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sd = sd
        return self

    def with_sdf(self, sdf: Optional[Sdf]) -> "SdgBuilder":
        """Set the sdf attribute (legacy).

        Args:
            sdf: Sdf value

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sdf = sdf
        return self

    def with_sdg(self, sdg: Optional["Sdg"]) -> "SdgBuilder":
        """Set the sdg attribute (legacy).

        Args:
            sdg: Sdg value

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sdg = sdg
        return self

    def with_sdx(self, sdx: Optional[Referrable]) -> "SdgBuilder":
        """Set the sdx attribute (legacy).

        Args:
            sdx: Referrable value

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sdx = sdx
        return self

    def with_sdxf(self, sdxf: Optional[Referrable]) -> "SdgBuilder":
        """Set the sdxf attribute (legacy).

        Args:
            sdxf: Referrable value

        Returns:
            self for method chaining
        """
        obj = self._get_instance()
        obj.sdxf = sdxf
        return self

    def build(self) -> Sdg:
        """Build and return the Sdg object.

        Returns:
            The constructed Sdg object
        """
        obj = self._get_instance()
        if obj is None:
            obj = Sdg()
        return obj
