"""MacSecKayParticipant AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_crypto_algo_config import (
    MacSecCryptoAlgoConfig,
)


class MacSecKayParticipant(Identifiable):
    """AUTOSAR MacSecKayParticipant."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ckn_ref: Optional[ARRef]
    crypto_algo: Optional[MacSecCryptoAlgoConfig]
    sak_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize MacSecKayParticipant."""
        super().__init__()
        self.ckn_ref: Optional[ARRef] = None
        self.crypto_algo: Optional[MacSecCryptoAlgoConfig] = None
        self.sak_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize MacSecKayParticipant to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MacSecKayParticipant, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ckn_ref
        if self.ckn_ref is not None:
            serialized = ARObject._serialize_item(self.ckn_ref, "CryptoServiceKey")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CKN-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_algo
        if self.crypto_algo is not None:
            serialized = ARObject._serialize_item(self.crypto_algo, "MacSecCryptoAlgoConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-ALGO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sak_ref
        if self.sak_ref is not None:
            serialized = ARObject._serialize_item(self.sak_ref, "CryptoServiceKey")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SAK-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecKayParticipant":
        """Deserialize XML element to MacSecKayParticipant object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacSecKayParticipant object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MacSecKayParticipant, cls).deserialize(element)

        # Parse ckn_ref
        child = ARObject._find_child_element(element, "CKN-REF")
        if child is not None:
            ckn_ref_value = ARRef.deserialize(child)
            obj.ckn_ref = ckn_ref_value

        # Parse crypto_algo
        child = ARObject._find_child_element(element, "CRYPTO-ALGO")
        if child is not None:
            crypto_algo_value = ARObject._deserialize_by_tag(child, "MacSecCryptoAlgoConfig")
            obj.crypto_algo = crypto_algo_value

        # Parse sak_ref
        child = ARObject._find_child_element(element, "SAK-REF")
        if child is not None:
            sak_ref_value = ARRef.deserialize(child)
            obj.sak_ref = sak_ref_value

        return obj



class MacSecKayParticipantBuilder:
    """Builder for MacSecKayParticipant."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacSecKayParticipant = MacSecKayParticipant()

    def build(self) -> MacSecKayParticipant:
        """Build and return MacSecKayParticipant object.

        Returns:
            MacSecKayParticipant instance
        """
        # TODO: Add validation
        return self._obj
